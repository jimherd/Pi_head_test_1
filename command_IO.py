# This Python file uses the following encoding: utf-8

import serial
import random
import time
import os
import array as arr

from enum import Enum, IntEnum
from itertools import repeat

import Sys_err
import Command_IO

import Pi_the_robot
import Globals
from Constants import *
from Pi_sound import *
from Sequences import *

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
    SET_FORM      = 0
    GET_FORM      = 1
    SET_CONTRAST  = 2
    READ_BUTTON   = 3

# class MessageCode(IntEnum):
#     OK                               = 0,
#     LETTER_ERROR                     = -100,   # rp2040 generated errors
#     DOT_ERROR                        = -101,
#     PLUSMINUS_ERROR                  = -102,
#     BAD_COMMAND                      = -103,
#     BAD_PORT_NUMBER                  = -104,
#     BAD_NOS_PARAMETERS               = -105,
#     BAD_BASE_PARAMETER               = -106,
#     PARAMETER_OUTWITH_LIMITS         = -107,
#     BAD_SERVO_COMMAND                = -108,
#     STEPPER_CALIBRATE_FAIL           = -109,
#     BAD_STEPPER_COMMAND              = -110,
#     BAD_STEP_VALUE                   = -111,
#     MOVE_ON_UNCALIBRATED_MOTOR       = -112,
#     EXISTING_FAULT_WITH_MOTOR        = -113,
#     SM_MOVE_TOO_SMALL                = -114,
#     LIMIT_SWITCH_ERROR               = -115,
#     UNKNOWN_STEPPER_MOTOR_STATE      = -116,
#     STEPPER_BUSY                     = -117,
#     SERVO_BUSY                       = -118,
#     GEN4_uLCD_NOT_DETECTED           = -119,
#     GEN4_uLCD_WRITE_OBJ_FAIL         = -120,
#     GEN4_uLCD_WRITE_OBJ_TIMEOUT      = -121,
#     GEN4_uLCD_WRITE_CONTRAST_FAIL    = -122,
#     GEN4_uLCD_WRITE_CONTRAST_TIMEOUT = -123,   
#     GEN4_uLCD_READ_OBJ_FAIL          = -124,
#     GEN4_uLCD_READ_OBJ_TIMEOUT       = -125,
#     GEN4_uLCD_CMD_BAD_FORM_INDEX     = -126,
#     GEN4_uLCD_WRITE_STR_TOO_BIG      = -127,
#     GEN4_uLCD_WRITE_STRING_FAIL      = -128,
#     GEN4_uLCD_WRITE_STRING_TIMEOUT   = -129,
#     GEN4_uLCD_BUTTON_FORM_INACTIVE   = -130,
#     QUOTE_ERROR                      = -131,
    

#     BAD_COMPORT_OPEN                = -200     # PC/Pi errors
#     UNKNOWN_COM_PORT                = -201
#     BAD_COMPORT_READ                = -202
#     BAD_COMPORT_WRITE               = -203
#     NULL_EMPTY_STRING               = -204
#     BAD_COMPORT_CLOSE               = -205
#     BAD_STRING_PARSE                = -206
#     BAD_JOINT_CODE                  = -207,
#     BAD_SERVO_POSITION              = -208,
#     BAD_SPEED_VALUE                 = -209,
#     FILE_NOT_FOUND                  = -210,
#     COMMAND_FILE_NOT_FOUND          = -211,

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

current_pose   = arr.array('i', repeat(0, (Sys_values.NOS_SERVOS + Sys_values.NOS_STEPPERS)))

argc: int = 0
int_parameter   = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))
float_parameter = arr.array('f', repeat(0, MAX_COMMAND_PARAMETERS))
param_type      = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))
reply_string: str = ""
reply_tmp_byte_string: str = ""

def command_IO_init() -> None:
    global ser
    ser = serial.Serial()
    argc = 0
    int_parameter   = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))
    float_parameter = arr.array('f', repeat(0, MAX_COMMAND_PARAMETERS))
    param_type      = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))

def init_sys(comport: str) -> Sys_err.MessageCode:
    command_IO_init()
    if (Sys_values.TEST_MODE == False):
        status = Command_IO.open_port(comport, Sys_values.PI_HEAD_BAUD_RATE)
        if ( status !=  Sys_err.MessageCode.OK):
            Pi_the_robot.sys_print("Fail to open port")
            return status
        status = Command_IO.ping()
        if ( status !=  Sys_err.MessageCode.OK):
            Pi_the_robot.sys_print("Fail to Ping board")
            return status
    init_sound_output()
    return Sys_err.MessageCode.OK

def open_port(port: int, baud_rate: int) -> Sys_err.MessageCode:
    ser.baudrate = baud_rate
    ser.timeout = READ_TIMEOUT
    ser.port = port
    ser.timeout = 5
    try:
        ser.open()
    except serial.SerialException as var : # var contains details of issue:
        return Sys_err.MessageCode.BAD_COMPORT_OPEN
    ser.flushInput()
    ser.timeout = 5
    return Sys_err.MessageCode.OK

def close_port() -> Sys_err.MessageCode:
    ser.close()
    return Sys_err.MessageCode.OK

def send_command(send_string: str) -> Sys_err.MessageCode:
    if(ser.isOpen() == False):
        return Sys_err.MessageCode.BAD_COMPORT_WRITE
    ser.write(str.encode(send_string)) # convert to bytes
    return Sys_err.MessageCode.OK

def get_reply() -> Sys_err.MessageCode:
    reply_string = ser.read_until(b'\n', 50)
    if (len(reply_string) == 0):
        return Sys_err.MessageCode.BAD_COMPORT_READ
    else:
        return Sys_err.MessageCode.OK

def do_command(cmd_string: str, first_int: int) -> Sys_err.MessageCode:
    status = send_command(cmd_string)
    if(status != Sys_err.MessageCode.OK):
        return status
    status = get_reply()
    if(status != Sys_err.MessageCode.OK):
        return status
    status = Parse_string(reply_string)
    if(status != Sys_err.MessageCode.OK):
        return status
    status = int_parameter[1]
    return status

def Parse_string(string_data: str) -> Sys_err.MessageCode:
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

    return Sys_err.MessageCode.OK

# ===========================================================================
# ping code

def ping() -> Sys_err.MessageCode:
    cmd_string = "ping 0 " + str(random.randint(1,98)) + "\n"
    first_val = 0
    status =  do_command(cmd_string, first_val)
    Pi_the_robot.sys_print(status)
    return status

# ===========================================================================
# servo code

def Execute_servo_cmd(joint: int, position: int, speed: int, group: bool) -> Sys_err.MessageCode:
    status = check_joint_data(joint, position, speed)
    if (status != Sys_err.MessageCode.OK):
        return status
# select type of move command
    if ((group == False) and (speed < Sys_values.SPEED_THRESHOLD)):
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
    first_val = 0
    status =  do_command(cmd_string, first_val)
    if (status == Sys_err.MessageCode.OK):
        current_pose[joint] = position  # record new position
    Pi_the_robot.sys_print(status)
    return status

def Mouth_on_off(mouthstate: bool, group: bool) -> Sys_err.MessageCode:
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
    first_val = 0
    status =  do_command(cmd_string, first_val)
    if (status == Sys_err.MessageCode.OK): 
        if (mouth_state == Mouth.OFF):
            mouth_state = Mouth.ON
            current_pose[Joints.MOUTH] = 45
        else:
            mouth_state = Mouth.OFF
            current_pose[Joints.mouth] = 0
    Pi_the_robot.sys_print(status)
    return status

def check_joint_data(joint: int, position: int, speed: int) -> Sys_err.MessageCode:
    if ((joint < FIRST_JOINT) or (joint > LAST_JOINT)):
        return Sys_err.MessageCode.BAD_JOINT_CODE
    if ((position < servo_data[joint][2]) or (position > servo_data[joint][3])):
        return Sys_err.MessageCode.BAD_SERVO_POSITION
    if ((position < servo_data[joint][4]) or (position > servo_data[joint][5])):
        return Sys_err.MessageCode.BAD_SPEED_VALUE
    return Sys_err.MessageCode.OK
    

# ===========================================================================
# Stepper motor code

def execute_stepper_cmd(stepper_no, stepper_cmd, stepper_speed_profile, stepper_step_value) -> Sys_err.MessageCode:
    cmd_string =(f"stepper {Sys_values.DEFAULT_PORT} {stepper_cmd} {stepper_no} {stepper_step_value}\n")
    first_val = 0
    status =  do_command(cmd_string, first_val)
    Pi_the_robot.sys_print(status)
    return status

# ===========================================================================
# Display code

def page_update(page_index) -> Sys_err.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SET_FORM} {page_index}\n")
    first_val = 0
    status =  do_command(cmd_string, first_val)
    Pi_the_robot.sys_print(status)
    return status

def string_update(self) -> None:
    pass

def read_button(button_index: int) -> Sys_err.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.READ_BUTTON} {button_index}\n")
    first_val = 0
    status =  do_command(cmd_string, first_val)
    Pi_the_robot.sys_print(status)
    return status

# ===========================================================================
# run sequences of commands from a list
#
# check for local commands (speak, ...) before sending remote command
# to the rp2040 MCU that controls the robot head hardware

def run_sequence(sequence) -> Sys_err.MessageCode:
    for i in range(len(sequence)):
        cmd_argv = sequence[i].split()

# execute command
        match cmd_argv[0]:
            case "speak":
                say_list = cmd_argv[3:]
                sentence = " ".join(say_list)
                block = False
                if (cmd_argv[2] == "w"):
                    block = True
                if (cmd_argv[1] == "f"):
                    try:
                        file = open(cmd_argv[3], 'r')
                    except FileNotFoundError:
                        print('This file does not exist')
                        return Sys_err.MessageCode.FILE_NOT_FOUND
                    while True:
                        text_line = file.readline()
                        if not text_line:
                            break
                        play_TTS_string(text_line, block)
                        TTS_wait_finish()
                    file.close()
                else:
                    play_TTS_string(sentence, block)
            case "plays":
                block = False
                if (cmd_argv[1] == "-b"):
                    block = True
                play_sound_file(cmd_argv[2], block)
            case "delay":
                delay = int(cmd_argv[1])
                time.sleep(delay)
            case _:          # must be a remote command
                first_val = 0
                cmd_string = sequence[i]  + '\n'  #   (f"{sequences[sequence_index][i]}\n")
                Pi_the_robot.sys_print("cmd =", cmd_string)
                status =  do_command(cmd_string, first_val)
                if (status != Sys_err.MessageCode.OK):
                    return status
 # exit               
    return Sys_err.MessageCode.OK

# ===========================================================================
# run sequences of commands from a text file
#

def run_file_sequence(filename: str) -> Sys_err.MessageCode:
    try:
        text_data = open(filename, 'r')
    except FileNotFoundError:
        print(f'Cannot open file {filename}')
        return Sys_err.MessageCode.COMMAND_FILE_NOT_FOUND
    data = text_data.read()            # read raw text data from text file
    cmd_list = data.splitlines(False)  # convert to list of commands and 
                                       # delete line separators
    text_data.close() 

    status = run_sequence(cmd_list)
    Pi_the_robot.sys_print("sequence : ", filename, " status = ", status)
