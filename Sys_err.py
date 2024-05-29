#
# sys_err : list of system error codes
#

from enum import Enum, IntEnum

class ErrorCode(IntEnum):
    OK                               = 0,
    LETTER_ERROR                     = -100,   # rp2040 generated errors
    DOT_ERROR                        = -101,
    PLUSMINUS_ERROR                  = -102,
    BAD_COMMAND                      = -103,
    BAD_PORT_NUMBER                  = -104,
    BAD_NOS_PARAMETERS               = -105,
    BAD_BASE_PARAMETER               = -106,
    PARAMETER_OUTWITH_LIMITS         = -107,
    BAD_SERVO_COMMAND                = -108,
    STEPPER_CALIBRATE_FAIL           = -109,
    BAD_STEPPER_COMMAND              = -110,
    BAD_STEP_VALUE                   = -111,
    MOVE_ON_UNCALIBRATED_MOTOR       = -112,
    EXISTING_FAULT_WITH_MOTOR        = -113,
    SM_MOVE_TOO_SMALL                = -114,
    LIMIT_SWITCH_ERROR               = -115,
    UNKNOWN_STEPPER_MOTOR_STATE      = -116,
    STEPPER_BUSY                     = -117,
    SERVO_BUSY                       = -118,
    GEN4_uLCD_NOT_DETECTED           = -119,
    GEN4_uLCD_WRITE_OBJ_FAIL         = -120,
    GEN4_uLCD_WRITE_OBJ_TIMEOUT      = -121,
    GEN4_uLCD_WRITE_CONTRAST_FAIL    = -122,
    GEN4_uLCD_WRITE_CONTRAST_TIMEOUT = -123,   
    GEN4_uLCD_READ_OBJ_FAIL          = -124,
    GEN4_uLCD_READ_OBJ_TIMEOUT       = -125,
    GEN4_uLCD_CMD_BAD_FORM_INDEX     = -126,
    GEN4_uLCD_WRITE_STR_TOO_BIG      = -127,
    GEN4_uLCD_WRITE_STRING_FAIL      = -128,
    GEN4_uLCD_WRITE_STRING_TIMEOUT   = -129,
    GEN4_uLCD_BUTTON_FORM_INACTIVE   = -130,
    QUOTE_ERROR                      = -131,
    

    BAD_COMPORT_OPEN                = -200     # PC/Pi errors
    UNKNOWN_COM_PORT                = -201
    BAD_COMPORT_READ                = -202
    BAD_COMPORT_WRITE               = -203
    NULL_EMPTY_STRING               = -204
    BAD_COMPORT_CLOSE               = -205
    BAD_STRING_PARSE                = -206
    BAD_JOINT_CODE                  = -207,
    BAD_SERVO_POSITION              = -208,
    BAD_SPEED_VALUE                 = -209,
    FILE_NOT_FOUND                  = -210,
    COMMAND_FILE_NOT_FOUND          = -211,