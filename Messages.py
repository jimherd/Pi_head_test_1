#
# Messages.py : list of system message codes
#
#    Codes                  Intent
#    =====                  ======
#    +1 => +99       information codes-
#        0            OK : successful execution of action
#  -100 => -199      error codes from microcontroller
#  -200 => -299      errorfrom PC/Rasperry Pi

from enum import Enum, IntEnum

class MessageCode(IntEnum):
    COM_PORT_OPEN_OK                 = 1

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
    NO_COM_PORT_FOUND               = -212
    LAST_ENTRY                      = -10000

Message_string_dict = {
    MessageCode.OK:                              "All is OK",
    MessageCode.LETTER_ERROR:                    "letter in number string",
    MessageCode.DOT_ERROR:                       "dot error in number string",
    MessageCode.PLUSMINUS_ERROR:                 "plus minus in wrong placein string",
    MessageCode.BAD_COMMAND:                     "Unknown PICO command",
    MessageCode.BAD_PORT_NUMBER:                 "bad port number",
    MessageCode.BAD_NOS_PARAMETERS:              "wrong number of parameters",
    MessageCode.BAD_BASE_PARAMETER:              "",
    MessageCode.PARAMETER_OUTWITH_LIMITS:        "a parameter is outwith set limits",
    MessageCode.BAD_SERVO_COMMAND:               "bad servo command",
    MessageCode.STEPPER_CALIBRATE_FAIL:          "stepper motor failed to calibrate",
    MessageCode.BAD_STEPPER_COMMAND:             "bad stepper motor command",
    MessageCode.BAD_STEP_VALUE:                  "bad stepper motor step value",
    MessageCode.MOVE_ON_UNCALIBRATED_MOTOR:      "move failed as stepper motor is not calibrated",
    MessageCode.EXISTING_FAULT_WITH_MOTOR:        "currently, motor has a fault",
    MessageCode.SM_MOVE_TOO_SMALL:                "stepper motor move request is too small",
    MessageCode.LIMIT_SWITCH_ERROR:               "failed to detect limit switch",
    MessageCode.UNKNOWN_STEPPER_MOTOR_STATE:      "stepper motor in unknown state",
    MessageCode.STEPPER_BUSY:                     "stepper motor is busy",
    MessageCode.SERVO_BUSY:                       "servo is busy",
    MessageCode.GEN4_uLCD_NOT_DETECTED:           "display not detected",
    MessageCode.GEN4_uLCD_WRITE_OBJ_FAIL:         "display write object fail",
    MessageCode.GEN4_uLCD_WRITE_OBJ_TIMEOUT:      "display write object timeout",
    MessageCode.GEN4_uLCD_WRITE_CONTRAST_FAIL:    "display write contrast fail",
    MessageCode.GEN4_uLCD_WRITE_CONTRAST_TIMEOUT: "display write contrast timeout",
    MessageCode.GEN4_uLCD_READ_OBJ_FAIL:          "display read object fail",
    MessageCode.GEN4_uLCD_READ_OBJ_TIMEOUT:       "display read object timeout",
    MessageCode.GEN4_uLCD_CMD_BAD_FORM_INDEX:     "display wrong form index",
    MessageCode.GEN4_uLCD_WRITE_STR_TOO_BIG:      "display write string too big",
    MessageCode.GEN4_uLCD_WRITE_STRING_FAIL:      "display write string fail",
    MessageCode.GEN4_uLCD_WRITE_STRING_TIMEOUT:   "display write string timeout",
    MessageCode.GEN4_uLCD_BUTTON_FORM_INACTIVE:   "display button form is inactive",
    MessageCode.QUOTE_ERROR:                      "quote error in command",
    
    MessageCode.BAD_COMPORT_OPEN:                 "Cannot open serial port",
    MessageCode.UNKNOWN_COM_PORT:                 "unknown serial port",
    MessageCode.BAD_COMPORT_READ:                 "cannot read from serial port",
    MessageCode.BAD_COMPORT_WRITE:                "bad serial port write",
    MessageCode.NULL_EMPTY_STRING:                "null string",
    MessageCode.BAD_COMPORT_CLOSE:                "bad serial port close",
    MessageCode.BAD_STRING_PARSE:                 "fail in string parse",
    MessageCode.BAD_JOINT_CODE:                   "bad joint code",
    MessageCode.BAD_SERVO_POSITION:               "bad servo position",
    MessageCode.BAD_SPEED_VALUE:                  "bad speed value",
    MessageCode.FILE_NOT_FOUND:                   "file not found",
    MessageCode.COMMAND_FILE_NOT_FOUND:           "command file not found",
    MessageCode.NO_COM_PORT_FOUND:                "no serial port found"
}
#
# replaced with dictionary
#
# Message_string = [
#     [MessageCode.COM_PORT_OPEN_OK, "COM port now open"],
#     [MessageCode.OK, "All is OK"],
#     [MessageCode.LETTER_ERROR, "letter in number string"],
#     [MessageCode.DOT_ERROR, "dot error in number string"],
#     [MessageCode.PLUSMINUS_ERROR, "plus minus in wrong placein string"],
#     [MessageCode.BAD_COMMAND, "Unknown PICO command"],
#     [MessageCode.BAD_PORT_NUMBER,"bad port number"],
#     [MessageCode.BAD_NOS_PARAMETERS,"wrong number of parameters"],
#     [MessageCode.BAD_BASE_PARAMETER,""],
#     [MessageCode.PARAMETER_OUTWITH_LIMITS,"a parameter is outwith set limits"],
#     [MessageCode.BAD_SERVO_COMMAND,"bad servo command"],
#     [MessageCode.STEPPER_CALIBRATE_FAIL,"stepper motor failed to calibrate"],
#     [MessageCode.BAD_STEPPER_COMMAND,"bad stepper motor command"],
#     [MessageCode.BAD_STEP_VALUE,"bad stepper motor step value"],
#     [MessageCode.MOVE_ON_UNCALIBRATED_MOTOR,"move failed as stepper motor is not calibrated"],
#     [MessageCode.EXISTING_FAULT_WITH_MOTOR,"currently, motor has a fault"],
#     [MessageCode.SM_MOVE_TOO_SMALL,"stepper motor move request is too small"],
#     [MessageCode.LIMIT_SWITCH_ERROR,"failed to detect limit switch"],
#     [MessageCode.UNKNOWN_STEPPER_MOTOR_STATE,"stepper motor in unknown state"],
#     [MessageCode.STEPPER_BUSY,"stepper motor is busy"],
#     [MessageCode.SERVO_BUSY,"servo is busy"],
#     [MessageCode.GEN4_uLCD_NOT_DETECTED,"display not detected"],
#     [MessageCode.GEN4_uLCD_WRITE_OBJ_FAIL,"display write object fail"],
#     [MessageCode.GEN4_uLCD_WRITE_OBJ_TIMEOUT,"display write object timeout"],
#     [MessageCode.GEN4_uLCD_WRITE_CONTRAST_FAIL,"display write contrast fail"],
#     [MessageCode.GEN4_uLCD_WRITE_CONTRAST_TIMEOUT,"display write contrast timeout"],
#     [MessageCode.GEN4_uLCD_READ_OBJ_FAIL,"display read object fail"],
#     [MessageCode.GEN4_uLCD_READ_OBJ_TIMEOUT,"display read object timeout"],
#     [MessageCode.GEN4_uLCD_CMD_BAD_FORM_INDEX,"display wrong form index"],
#     [MessageCode.GEN4_uLCD_WRITE_pyttsx3STR_TOO_BIG,"display write string too big"],
#     [MessageCode.GEN4_uLCD_WRITE_STRING_FAIL,"display write string fail"],
#     [MessageCode.GEN4_uLCD_WRITE_STRING_TIMEOUT,"display write string timeout"],
#     [MessageCode.GEN4_uLCD_BUTTON_FORM_INACTIVE,"display button form is inactive"],
#     [MessageCode.QUOTE_ERROR,"quote error in command"],
    

#     [MessageCode.BAD_COMPORT_OPEN,"Cannot open com port"],
#     [MessageCode.UNKNOWN_COM_PORT,"unknown com port"],
#     [MessageCode.BAD_COMPORT_READ,"bad comport read"],
#     [MessageCode.BAD_COMPORT_WRITE,"bad com port write"],
#     [MessageCode.NULL_EMPTY_STRING,"null string"],
#     [MessageCode.BAD_COMPORT_CLOSE,"bad com port close"],
#     [MessageCode.BAD_STRING_PARSE,"fail in string parse"],
#     [MessageCode.BAD_JOINT_CODE,"bad joint code"],
#     [MessageCode.BAD_SERVO_POSITION,"bad servo position"],
#     [MessageCode.BAD_SPEED_VALUE,"bad speed value"],
#     [MessageCode.FILE_NOT_FOUND,"file not found"],
#     [MessageCode.COMMAND_FILE_NOT_FOUND,"command file not found"],
#     [MessageCode.NO_COM_PORT_FOUND,"no com port found"],
# ]