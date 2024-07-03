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
    LAST_ENTRY                      = -10000


Error_String = [
    [ErrorCode.OK, "All is OK"],
    [ErrorCode.LETTER_ERROR, "letter in number string"],
    [ErrorCode.DOT_ERROR, "dot error in number string"],
    [ErrorCode.PLUSMINUS_ERROR, "plus minus in wrong placein string"],
    [ErrorCode.BAD_COMMAND, "Unknown PICO command"],
    [ErrorCode.BAD_PORT_NUMBER,"bad port number"],
    [ErrorCode.BAD_NOS_PARAMETERS,"wrong number of parameters"],
    [ErrorCode.BAD_BASE_PARAMETER,""],
    [ErrorCode.PARAMETER_OUTWITH_LIMITS,"a parameter is outwith set limits"],
    [ErrorCode.BAD_SERVO_COMMAND,"bad servo command"],
    [ErrorCode.STEPPER_CALIBRATE_FAIL,"stepper motor failed to calibrate"],
    [ErrorCode.BAD_STEPPER_COMMAND,"bad stepper motor command"],
    [ErrorCode.BAD_STEP_VALUE,"bad stepper motor step value"],
    [ErrorCode.MOVE_ON_UNCALIBRATED_MOTOR,"move failed as stepper motor is not calibrated"],
    [ErrorCode.EXISTING_FAULT_WITH_MOTOR,"currently, motor has a fault"],
    [ErrorCode.SM_MOVE_TOO_SMALL,"stepper motor move request is too small"],
    [ErrorCode.LIMIT_SWITCH_ERROR,"failed to detect limit switch"],
    [ErrorCode.UNKNOWN_STEPPER_MOTOR_STATE,"stepper motor in unknown state"],
    [ErrorCode.STEPPER_BUSY,"stepper motor is busy"],
    [ErrorCode.SERVO_BUSY,"servo is busy"],
    [ErrorCode.GEN4_uLCD_NOT_DETECTED,"display not detected"],
    [ErrorCode.GEN4_uLCD_WRITE_OBJ_FAIL,"display write object fail"],
    [ErrorCode.GEN4_uLCD_WRITE_OBJ_TIMEOUT,"display write object timeout"],
    [ErrorCode.GEN4_uLCD_WRITE_CONTRAST_FAIL,"display write contrast fail"],
    [ErrorCode.GEN4_uLCD_WRITE_CONTRAST_TIMEOUT,"display write contrast timeout"],
    [ErrorCode.GEN4_uLCD_READ_OBJ_FAIL,"display read object fail"],
    [ErrorCode.GEN4_uLCD_READ_OBJ_TIMEOUT,"display read object timeout"],
    [ErrorCode.GEN4_uLCD_CMD_BAD_FORM_INDEX,"display wrong form index"],
    [ErrorCode.GEN4_uLCD_WRITE_STR_TOO_BIG,"display write string too big"],
    [ErrorCode.GEN4_uLCD_WRITE_STRING_FAIL,"display write string fail"],
    [ErrorCode.GEN4_uLCD_WRITE_STRING_TIMEOUT,"display write string timeout"],
    [ErrorCode.GEN4_uLCD_BUTTON_FORM_INACTIVE,"display button form is inactive"],
    [ErrorCode.QUOTE_ERROR,"quote error in command"],
    

    [ErrorCode.BAD_COMPORT_OPEN,"Cannot open com port"],
    [ErrorCode.UNKNOWN_COM_PORT,"unknown com port"],
    [ErrorCode.BAD_COMPORT_READ,"bad comport read"],
    [ErrorCode.BAD_COMPORT_WRITE,"bad com port write"],
    [ErrorCode.NULL_EMPTY_STRING,"null string"],
    [ErrorCode.BAD_COMPORT_CLOSE,"bad com port close"],
    [ErrorCode.BAD_STRING_PARSE,"fail in string parse"],
    [ErrorCode.BAD_JOINT_CODE,"bad joint code"],
    [ErrorCode.BAD_SERVO_POSITION,"bad servo position"],
    [ErrorCode.BAD_SPEED_VALUE,"bad speed value"],
    [ErrorCode.FILE_NOT_FOUND,"file not found"],
    [ErrorCode.COMMAND_FILE_NOT_FOUND,"command file not found"]
]


Error_String_dict = {
    ErrorCode.OK:                              "All is OK",
    ErrorCode.LETTER_ERROR:                    "letter in number string",
    ErrorCode.DOT_ERROR:                       "dot error in number string",
    ErrorCode.PLUSMINUS_ERROR:                 "plus minus in wrong placein string",
    ErrorCode.BAD_COMMAND:                     "Unknown PICO command",
    ErrorCode.BAD_PORT_NUMBER:                 "bad port number",
    ErrorCode.BAD_NOS_PARAMETERS:              "wrong number of parameters",
    ErrorCode.BAD_BASE_PARAMETER:              "",
    ErrorCode.PARAMETER_OUTWITH_LIMITS:        "a parameter is outwith set limits",
    ErrorCode.BAD_SERVO_COMMAND:               "bad servo command",
    ErrorCode.STEPPER_CALIBRATE_FAIL:          "stepper motor failed to calibrate",
    ErrorCode.BAD_STEPPER_COMMAND:             "bad stepper motor command",
    ErrorCode.BAD_STEP_VALUE:                  "bad stepper motor step value",
    ErrorCode.MOVE_ON_UNCALIBRATED_MOTOR:      "move failed as stepper motor is not calibrated",
    ErrorCode.EXISTING_FAULT_WITH_MOTOR:        "currently, motor has a fault",
    ErrorCode.SM_MOVE_TOO_SMALL:                "stepper motor move request is too small",
    ErrorCode.LIMIT_SWITCH_ERROR:               "failed to detect limit switch",
    ErrorCode.UNKNOWN_STEPPER_MOTOR_STATE:      "stepper motor in unknown state",
    ErrorCode.STEPPER_BUSY:                     "stepper motor is busy",
    ErrorCode.SERVO_BUSY:                       "servo is busy",
    ErrorCode.GEN4_uLCD_NOT_DETECTED:           "display not detected",
    ErrorCode.GEN4_uLCD_WRITE_OBJ_FAIL:         "display write object fail",
    ErrorCode.GEN4_uLCD_WRITE_OBJ_TIMEOUT:      "display write object timeout",
    ErrorCode.GEN4_uLCD_WRITE_CONTRAST_FAIL:    "display write contrast fail",
    ErrorCode.GEN4_uLCD_WRITE_CONTRAST_TIMEOUT: "display write contrast timeout",
    ErrorCode.GEN4_uLCD_READ_OBJ_FAIL:          "display read object fail",
    ErrorCode.GEN4_uLCD_READ_OBJ_TIMEOUT:       "display read object timeout",
    ErrorCode.GEN4_uLCD_CMD_BAD_FORM_INDEX:     "display wrong form index",
    ErrorCode.GEN4_uLCD_WRITE_STR_TOO_BIG:      "display write string too big",
    ErrorCode.GEN4_uLCD_WRITE_STRING_FAIL:      "display write string fail",
    ErrorCode.GEN4_uLCD_WRITE_STRING_TIMEOUT:   "display write string timeout",
    ErrorCode.GEN4_uLCD_BUTTON_FORM_INACTIVE:   "display button form is inactive",
    ErrorCode.QUOTE_ERROR:                      "quote error in command",
    
    ErrorCode.BAD_COMPORT_OPEN:                 "Cannot open com port",
    ErrorCode.UNKNOWN_COM_PORT:                 "unknown com port",
    ErrorCode.BAD_COMPORT_READ:                 "bad comport read",
    ErrorCode.BAD_COMPORT_WRITE:                "bad com port write",
    ErrorCode.NULL_EMPTY_STRING:                "null string",
    ErrorCode.BAD_COMPORT_CLOSE:                "bad com port close",
    ErrorCode.BAD_STRING_PARSE:                 "fail in string parse",
    ErrorCode.BAD_JOINT_CODE:                   "bad joint code",
    ErrorCode.BAD_SERVO_POSITION:               "bad servo position",
    ErrorCode.BAD_SPEED_VALUE:                  "bad speed value",
    ErrorCode.FILE_NOT_FOUND:                   "file not found",
    ErrorCode.COMMAND_FILE_NOT_FOUND:           "command file not found",
}


def speak_error(err_code: ErrorCode) -> None:
    pass