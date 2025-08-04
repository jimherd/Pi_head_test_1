# This Python file uses the following encoding: utf-8

import random
import time
import array as arr

from enum import Enum, IntEnum
from itertools import repeat

import serial
import serial.tools.list_ports


import Messages
#import Command_IO

import Pi_the_robot
import Globals
from Constants  import *
from Pi_sound   import *
from Sequences  import *
from IMX500_sys import *

import Comms_IO

Pi_head_com_port = ""
MAX_COMMAND_PARAMETERS = 10
READ_TIMEOUT = 4  # seconds
MAX_COMMAND_STRING_LENGTH = 100
MAX_REPLY_STRING_LENGTH = 100

class Joints(IntEnum):
    RIGHT_EYE_LR    = 0
    RIGHT_EYE_UD    = 1
    RIGHT_EYE_LID   = 2
    RIGHT_EYE_BROW  = 3
    LEFT_EYE_LR     = 4
    LEFT_EYE_UD     = 5
    LEFT_EYE_LID    = 6
    LEFT_EYE_BROW   = 7
    MOUTH           = 8

FIRST_JOINT = Joints.RIGHT_EYE_LR
LAST_JOINT  = Joints.LEFT_EYE_BROW

class Mouth(IntEnum):
    OFF  = 0
    ON   = 1

# servo number, servo  type, -ve max, +ve max, init value, min delay, max delay
servo_data = [  
    [Joints.RIGHT_EYE_LR,    servo_type.SERVO, -25, +25, 0, 0, 250],
    [Joints.RIGHT_EYE_UD,    servo_type.SERVO, -45, +45, 0, 0, 250],
    [Joints.RIGHT_EYE_LID,   servo_type.SERVO, -25, +25, 0, 0, 250],
    [Joints.RIGHT_EYE_BROW,  servo_type.SERVO, -30, +30, 0, 0, 250],
    [Joints.LEFT_EYE_LR,   servo_type.SERVO, -25, +25, 0, 0, 250],
    [Joints.LEFT_EYE_UD,   servo_type.SERVO, -45, +45, 0, 0, 250],
    [Joints.LEFT_EYE_LID,  servo_type.SERVO, -25, +25, 0, 0, 250],
    [Joints.LEFT_EYE_BROW, servo_type.SERVO, -30, +30, 0, 0, 250],
    [Joints.MOUTH,          servo_type.MOTOR, -30, +30, 0, 0, 250],
]

class Display_commands(IntEnum):
    SET_uLCD_FORM             = 0
    GET_uLCD_FORM             = 1
    SET_uLCD_CONTRAST         = 2
    READ_uLCD_BUTTON          = 3
    READ_uLCD_SWITCH          = 4
    READ_uLCD_OBJECT          = 5
    WRITE_uLCD_STRING         = 6
    WRITE_uLCD_OBJECT         = 7
    SCAN_uLCD_BUTTON_PRESSES  = 8

class Modes(IntEnum):
    MODE_U = 0
    MODE_I = 1
    MODE_R = 2
    MODE_S = 3

class ServoCommands(IntEnum):
    ABS_MOVE           = 0
    ABS_MOVE_SYNC      = 1
    SPEED_MOVE         = 2
    SPEED_MOVE_SYNC    = 3
    RUN_SYNC_MOVES     = 4
    STOP               = 5
    STOP_ALL           = 6
    DISABLE            = 7

class StepperCommands(IntEnum):
    REL_MOVE           = 0
    ABS_MOVE           = 1  
    REL_MOVE_SYNC      = 2
    ABS_MOVE_SYNC      = 3
    CALIBRATE          = 4

class NeopixelCommands(IntEnum):
    BLANK_ALL          = 0

current_pose   = arr.array('i', repeat(0, (Sys_values.NOS_SERVOS + Sys_values.NOS_STEPPERS)))

##########################################################################
# array structures to hold the parsed ASCII string that is returned
# from a RP2040 command

argc: int = 0
int_parameter   = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))
float_parameter = arr.array('f', repeat(0, MAX_COMMAND_PARAMETERS))
param_type      = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))
reply_string: str = ""
reply_tmp_byte_string: str = ""

##########################################################################

def command_IO_init() -> None:
    Comms_IO.get_coms_info()
    global ser              # allow access to serial port from other routines
    ser = serial.Serial()
    # argc = 0
    # int_parameter   = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))
    # float_parameter = arr.array('f', repeat(0, MAX_COMMAND_PARAMETERS))
    # param_type      = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))

def init_sys(comport: str) -> Messages.MessageCode:
    command_IO_init()
    if (Sys_values.TEST_MODE == False):
        status = open_port(comport, Sys_values.PI_HEAD_BAUD_RATE)
        if ( status !=  Messages.MessageCode.OK):
            Pi_the_robot.sys_print("Fail to open port")
            return status
        status = ping()
        if ( status !=  Messages.MessageCode.OK):
            Pi_the_robot.sys_print("Fail to Ping board")
            return status
    # init_sound_output()
    return Messages.MessageCode.OK

def open_port(port: int, baud_rate: int) -> Messages.MessageCode:
    ser.baudrate = baud_rate
    ser.timeout = READ_TIMEOUT
    ser.port = port
    ser.timeout = 5
    try:
        ser.open()
    except serial.SerialException:             
        return Messages.MessageCode.BAD_COMPORT_OPEN
    ser.flushInput()
    ser.timeout = 5
    return Messages.MessageCode.OK

def close_port() -> Messages.MessageCode:
    ser.close()
    return Messages.MessageCode.OK

def send_command(send_string: str) -> Messages.MessageCode:
    if(ser.isOpen() == False):
        return Messages.MessageCode.BAD_SERIAL_PORT_WRITE
    ser.write(str.encode(send_string)) # convert to bytes
    return Messages.MessageCode.OK

def get_reply() -> Messages.MessageCode:
    global reply_string
    reply_string = ser.read_until(b'\n', 50)
    if (len(reply_string) == 0):
        return Messages.MessageCode.BAD_SERIAL_PORT_READ
    else:
        return Messages.MessageCode.OK

#
# Data is returned through global 'int_parameter[] array

def do_command(cmd_string: str) -> Messages.MessageCode:
    status = send_command(cmd_string)
    if(status != Messages.MessageCode.OK):
        return status
    status = get_reply()
    if(status != Messages.MessageCode.OK):
        return status
    status = Parse_string(reply_string)
    return status

def Parse_string(string_data: str) -> Messages.MessageCode:
    global argc
    for index in range(MAX_COMMAND_PARAMETERS):
        int_parameter[index] = 0
        float_parameter[index] = 0.0
        param_type[index] = int(Modes.MODE_U)
        argc = 0
    # break string into a list of strings
    string_parameters = string_data.split()
    argc = len(string_parameters)
    Pi_the_robot.sys_print(reply_string)

    for index in range(argc):
        flag = True
        try:
            int(string_parameters[index])
        except ValueError:
            flag = False
        if (flag == True):
            int_parameter[index] = int(string_parameters[index])
            param_type[index] = Modes.MODE_I
            continue

        flag = True
        try:
            float(string_parameters[index])
        except ValueError:
            flag = False
        if (flag == True):
            int_parameter[index] = float(string_parameters[index])
            param_type[index] = Modes.MODE_R
            Pi_the_robot.sys_print("float detected")
            continue

        param_type[index] = Modes.MODE_S
        Pi_the_robot.sys_print(int_parameter)
    return Messages.MessageCode.OK

# ===========================================================================
# ping code

def ping() -> Messages.MessageCode:
    cmd_string = "ping 0 " + str(random.randint(1,98)) + "\n"
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status

# ===========================================================================
# servo code

def Execute_servo_cmd(joint: int, position: int, speed: int, group: bool) -> Messages.MessageCode:
    status = check_joint_data(joint, position, speed)
    if (status != Messages.MessageCode.OK):
        return status
# select type of move command
    if ((group is False) and (speed < Sys_values.SPEED_THRESHOLD)):
        servo_cmd = ServoCommands.ABS_MOVE
    elif ((group == True) and (speed < Sys_values.SPEED_THRESHOLD)):
        servo_cmd = ServoCommands.ABS_MOVE_SYNC
    elif ((group == False) and (speed >= Sys_values.SPEED_THRESHOLD)):
        servo_cmd = ServoCommands.SPEED_MOVE
    else:
        servo_cmd = ServoCommands.SPEED_MOVE_SYNC
    # construct appropriate command string
    if (speed < Sys_values.SPEED_THRESHOLD):
        cmd_string =(f"servo {Sys_values.DEFAULT_PORT} {servo_cmd} {joint} {position}\n")
    else:
        cmd_string =(f"servo {Sys_values.DEFAULT_PORT} {servo_cmd} {joint} {position} {speed}\n")
# execute servo move command
    status =  do_command(cmd_string)
    if (status == Messages.MessageCode.OK):
        current_pose[joint] = position  # record new position
    Pi_the_robot.sys_print(status)
    return status

def Mouth_on_off(mouth_state: bool, group: bool) -> Messages.MessageCode:
    if (group == False):
        servo_cmd = ServoCommands.ABS_MOVE
    else:
        servo_cmd = ServoCommands.ABS_MOVE_SYNC

    if (mouth_state == Mouth.OFF):
        cmd_string = (f"servo {Sys_values.DEFAULT_PORT} {servo_cmd} 8 45\n")   # turn ON
        mouth_state = Mouth.ON
    else:
        cmd_string = (f"servo {Sys_values.DEFAULT_PORT} {servo_cmd} 8 0\n")   # turn OFF
        mouth_state = Mouth.OFF

    # execute servo move command
    status =  do_command(cmd_string)
    if (status == Messages.MessageCode.OK): 
        if (mouth_state == Mouth.OFF):
            mouth_state = Mouth.ON
            current_pose[Joints.MOUTH] = 45
        else:
            mouth_state = Mouth.OFF
            current_pose[Joints.MOUTH] = 0
    Pi_the_robot.sys_print(status)
    return status

def check_joint_data(joint: int, position: int, speed: int) -> Messages.MessageCode:
    if ((joint < FIRST_JOINT) or (joint > LAST_JOINT)):
        return Messages.MessageCode.BAD_JOINT_CODE
    if ((position < servo_data[joint][2]) or (position > servo_data[joint][3])):
        return Messages.MessageCode.BAD_SERVO_POSITION
    if ((position < servo_data[joint][4]) or (position > servo_data[joint][5])):
        return Messages.MessageCode.BAD_SPEED_VALUE
    return Messages.MessageCode.OK
    

# ===========================================================================
# Stepper motor code

def execute_stepper_cmd(stepper_no, stepper_cmd, stepper_speed_profile, stepper_step_value) -> Messages.MessageCode:
    cmd_string =(f"stepper {Sys_values.DEFAULT_PORT} {stepper_cmd} {stepper_no} {stepper_step_value}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status

# ===========================================================================
# Display code

# def set_display_form(page_index) -> Messages.MessageCode:
#     cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SET_uLCD_FORM} {page_index}\n")
#     status =  do_command(cmd_string)
#     Pi_the_robot.sys_print(status)
#     return status

# def get_display_form() -> Messages.MessageCode:
#     cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SET_uLCD_FORM}\n")
#     status =  do_command(cmd_string)
#     Pi_the_robot.sys_print(status)
#     return status

# def string_update() -> None:
#     pass

# def read_button(button_index: int) -> Messages.MessageCode:
#     cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.READ_uLCD_BUTTON} {button_index}\n")
#     status =  do_command(cmd_string)
#     Pi_the_robot.sys_print(status)
#     return status

# ===========================================================================
# run sequences of commands from a list
#
# check for local commands (speak, ...) before sending remote command
# to the rp2040 MCU that controls the robot head hardware

def run_sequence(sequence) -> Messages.MessageCode:
    for i in range(len(sequence)):
        cmd_argv = sequence[i].split()

# execute command
        match cmd_argv[0]:
            case "video":
                for count in range(cmd_argv[1]):  # number of image processing cycles
                    get_detections()
                    sleep(cmd_argv[2] * 0.1)    # delay between frames in units of 0.1sec
            case "speak":
                say_list = cmd_argv[3:]
                sentence = " ".join(say_list)
                block = False
                if (cmd_argv[2] == "w"):
                    block = True
                if (cmd_argv[1] == "f"):
                    try:
                        file = open(cmd_argv[3], 'r', encoding='utf-8')
                    except FileNotFoundError:
                        print('This file does not exist')
                        return Messages.MessageCode.FILE_NOT_FOUND
                    while True:
                        text_line = file.readline()
                        if not text_line:
                            break
                        say_espeak(text_line)
                    file.close()
                else:
                    say_espeak(sentence)
            case "plays":
                block = False
                if (cmd_argv[1] == "-b"):
                    block = True
                play_sound_file(cmd_argv[2], block)
            case "delay":
                delay = int(cmd_argv[1])
                time.sleep(delay) 
            case _:          # must be a remote command
                cmd_string = sequence[i]  + '\n'  #   (f"{sequences[sequence_index][i]}\n")
                Pi_the_robot.sys_print("cmd =", cmd_string)
                status =  do_command(cmd_string)
                if (status != Messages.MessageCode.OK):
                    return status
 # exit               
    return Messages.MessageCode.OK

# ===========================================================================
# run sequences of commands from a text file
#

def run_file_sequence(filename: str) -> Messages.MessageCode:
    try:
        text_data = open(filename, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f'Cannot open file {filename}')
        return Messages.MessageCode.COMMAND_FILE_NOT_FOUND
    data = text_data.read()            # read raw text data from text file
    cmd_list = data.splitlines(False)  # convert to list of commands and 
                                       # delete line separators
    text_data.close() 

    status = run_sequence(cmd_list)
    Pi_the_robot.sys_print("sequence : ", filename, " status = ", status)
