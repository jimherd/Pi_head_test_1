# This Python file uses the following encoding: utf-8

# note :  ._name is the convention to indicate non-public attributes

from enum import Enum, IntEnum, StrEnum

class Sys_values(IntEnum):   
    PI_HEAD_BAUD_RATE = 115200
    DEFAULT_PORT      = 9
    POWER_ON_SEQUENCE = 0
    SPEED_THRESHOLD   = 21
    NOS_SERVOS        = 8
    NOS_STEPPERS      = 1
    TEST_MODE         = False
    DEBUG_MODE        = True


class servo_type(IntEnum):
    SERVO = 0
    MOTOR = 1

class Sys_strings(StrEnum):
    PI_HEAD_COM_PORT  = "com3"
    INTRO_STRING      = "Hello"

class This_platform(IntEnum):
    UNKNOWN    = 0
    WINDOWS    = 1
    LINUX      = 2


