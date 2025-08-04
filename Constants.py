# This Python file uses the following encoding: utf-8
#
# note :  ._name is the convention to indicate non-public attributes

from enum import IntEnum, StrEnum

class Sys_values(IntEnum):   
    PI_HEAD_BAUD_RATE = 115200
    DEFAULT_PORT      = 9
    POWER_ON_SEQUENCE = 0
    SPEED_THRESHOLD   = 21
    NOS_SERVOS        = 8
    NOS_STEPPERS      = 1
    TEST_MODE         = False
    DEBUG_MODE        = True
    DEBUG_SPEAK_MODE  = True


class servo_type(IntEnum):
    SERVO = 0
    MOTOR = 1

class Sys_strings(StrEnum):
    WIN_COM_PORT = "com4"
 #   PI_COM_PORT  = "/dev/serial0"
    PI_COM_PORT = "/dev/ttyUSB0"  # Updated for Linux, typically used for USB serial devices
    INTRO_STRING = "Hello"

class This_platform(IntEnum):
    UNKNOWN    = 0
    WINDOWS    = 1
    LINUX      = 2

class forms(IntEnum):
    FORM0 = 0
    FORM1 = 1
    FORM2 = 2
    FORM3 = 3
    FORM4 = 4
    FORM5 = 5
    FORM6 = 6
    FORM7 = 7


