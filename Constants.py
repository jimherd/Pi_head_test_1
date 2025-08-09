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
    FORM_0 = 0
    FORM_1 = 1
    FORM_2 = 2
    FORM_3 = 3
    FORM_4 = 4
    FORM_5 = 5
    FORM_6 = 6
    FORM_7 = 7

class button_id(IntEnum):
    buttton_id_0 = 0
    buttton_id_1 = 1
    buttton_id_2 = 2
    buttton_id_3 = 3
    buttton_id_4 = 4
    buttton_id_5 = 5
    buttton_id_6 = 6
    buttton_id_7 = 7

class states(IntEnum):
    S0 = 0      # Root form,        FORM0
    S1 = 1      # Left eye tests,   FORM1
    S2 = 2      # Right eye tests,  FORM2
    S3 = 3
    S4 = 4
    S5 = 5
    S6 = 6
    S7 = 7
    S8 = 8



