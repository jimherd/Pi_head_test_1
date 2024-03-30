# This Python file uses the following encoding: utf-8

import serial
import random
import time
import os
import array as arr

from enum import Enum, IntEnum
from itertools import repeat

import Globals
import Command_IO
from Pi_sound import *
from Sequences import sequences

MAX_COMMAND_PARAMETERS = 10
READ_TIMEOUT = 4  # seconds
MAX_COMMAND_STRING_LENGTH = 100
MAX_REPLY_STRING_LENGTH = 100

class Joints(IntEnum):

    LEFT_EYE_RIGHT_LEFT  = 0
    LEFT_EYE_UP_DOWN     = 1
    LEFT_EYE_LID         = 2
    LEFT_EYE_BROW        = 3
    RIGHT_EYE_RIGHT_LEFT = 4
    RIGHT_EYE_UP_DOWN    = 5
    RIGHT_EYE_LID        = 6
    RIGHT_EYE_BROW       = 7
    MOUTH                = 8

class Display_commands(IntEnum):
    SET_FORM      = 0
    GET_FORM      = 1
    SET_CONTRAST  = 2
    READ_BUTTON   = 3

class ErrorCode(IntEnum):
    OK                              = 0
    LETTER_ERROR                    = -100    # rp2040 microcontroller errors
    DOT_ERROR                       = -101
    PLUSMINUS_ERROR                 = -102
    BAD_COMMAND                     = -103
    BAD_PORT_NUMBER                 = -104
    BAD_NOS_PARAMETERS              = -105
    BAD_BASE_PARAMETER              = -106
    PARAMETER_OUTWITH_LIMITS        = -107
    BAD_SERVO_COMMAND               = -108
    STEPPER_CALIBRATE_FAIL          = -109
    BAD_STEPPER_COMMAND             = -110
    BAD_STEP_VALUE                  = -111
    MOVE_ON_UNCALIBRATED_MOTOR      = -112
    EXISTING_FAULT_WITH_MOTOR       = -113
    SM_MOVE_TOO_SMALL               = -114
    LIMIT_SWITCH_ERROR              = -115
    UNKNOWN_STEPPER_MOTOR_STATE     = -116
    STEPPER_BUSY                    = -117
    SERVO_BUSY                      = -118

    BAD_COMPORT_OPEN                = -200     # PC/Pi errors
    UNKNOWN_COM_PORT                = -201
    BAD_COMPORT_READ                = -202
    BAD_COMPORT_WRITE               = -203
    NULL_EMPTY_STRING               = -204
    BAD_COMPORT_CLOSE               = -205
    BAD_STRING_PARSE                = -206

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

argc = 0
int_parameter   = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))
float_parameter = arr.array('f', repeat(0, MAX_COMMAND_PARAMETERS))
param_type      = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))
reply_string = ""
reply_tmp_byte_string = ""

#ser = None

def command_IO_init():
    global ser
    ser = serial.Serial()
    argc = 0
    int_parameter   = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))
    float_parameter = arr.array('f', repeat(0, MAX_COMMAND_PARAMETERS))
    param_type      = arr.array('i', repeat(0, MAX_COMMAND_PARAMETERS))

def open_port(port, baud_rate):
    ser.baudrate = baud_rate
    ser.timeout = READ_TIMEOUT
    ser.port = port
    ser.timeout = 5
    try:
        ser.open()
    except:
        return ErrorCode.BAD_COMPORT_OPEN
    ser.flushInput()
    ser.timeout = 5
    return ErrorCode.OK

def close_port():
    ser.close()
    return ErrorCode.OK

def send_command(send_string):
    if(ser.isOpen() == False):
        return ErrorCode.BAD_COMPORT_WRITE
    ser.write(str.encode(send_string)) # convert to bytes
    return ErrorCode.OK

def get_reply():
    reply_string = ser.read_until(b'\n', 50)
    if (len(reply_string) == 0):
        return ErrorCode.BAD_COMPORT_READ
    else:
        return ErrorCode.OK

def do_command(cmd_string, first_int):
    status = send_command(cmd_string)
    if(status != ErrorCode.OK):
        return status
    status = get_reply()
    if(status != ErrorCode.OK):
        return status
    status = Parse_string(reply_string)
    if(status != ErrorCode.OK):
        return status
    status = int_parameter[1]
    return status

def Parse_string(string_data):
    for index in range(MAX_COMMAND_PARAMETERS):
        int_parameter[index] = 0
        float_parameter[index] = 0.0
        param_type[index] = int(Modes.MODE_U)
        argc = 0
    # break string into a list of strings
    string_parameters = string_data.split()
    argc = len(string_parameters)
    print(reply_string)

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
            print("float detected")
            continue

        param_type[index] = Modes.MODE_S
        print(int_parameter)

    return ErrorCode.OK

# ===========================================================================
# ping code

def ping(self):
    cmd_string = "ping 0 " + str(random.randint(1,98)) + "\n"
    first_val = 0
    status =  do_command(self.cmd_string, first_val)
    print(status)
    return status

# ===========================================================================
# sequences code
#
# check for local commands (speak, ...) before sending remote command
# to the rp2040 MCU that controls the robot head hardware

def run_sequence(sequence_index):
    for i in range(len(sequences[sequence_index])):
        cmd_argv = sequences[sequence_index][i].split()
        match cmd_argv[0]:
            case "speak":
                say_list = cmd_argv[2:]
                sentence = " ".join(say_list)
                wait = False
                if (int(cmd_argv[1]) == 1):
                    wait = True
                play_TTS_string(sentence, wait)
            case "plays":
                play_sound_file(os.path.join(cmd_argv[1]))
            case "delay":
                delay = int(cmd_argv[1])
                time.sleep(delay)
            case _:          # must be a remote command
                first_val = 0
                cmd_string = sequences[sequence_index][i] + "\n"  #   (f"{sequences[sequence_index][i]}\n")
                status =  Command_IO.do_command(cmd_string, first_val)
                if (status != ErrorCode.OK):
                    return status
    return ErrorCode.OK


