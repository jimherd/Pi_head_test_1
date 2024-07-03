
#
# Module : Pi_the_robot
#
#from  Command_IO import ErrorCode
import Command_IO 
import Sys_err
from Globals    import  *
from Constants  import  *
from Pi_sound   import  *
from Sequences  import  *


# ===========================================================================
        
# def init_sys(comport: str) -> Command_IO.ErrorCode:
#     Command_IO.init()
#     if (Sys_values.TEST_MODE == False):
#         status = Command_IO.open_port(Sys_strings.PI_HEAD_COM_PORT, Sys_values.PI_HEAD_BAUD_RATE)
#         if ( status !=  Command_IO.ErrorCode.OK):
#             sys_print("Fail to open port")
#             return status
#         status = Command_IO.ping()
#         if ( status !=  Command_IO.ErrorCode.OK):
#             sys_print("Fail to Ping board")
#             return status
#     init_sound_output()
#     return Command_IO.ErrorCode.OK
#
# print if in debug mode
#

def sys_print(*args) -> None:
    if (Sys_values.DEBUG_MODE == True):
        #Iterate over all args, convert them to str, and join them
        args_str = ','.join(map(str,args))
        print(args_str)

def speak_error(err_code: Sys_err.ErrorCode) -> None:
    play_TTS_string(Sys_err.Error_String_dict[err_code], True)

def run_sys() -> Sys_err.ErrorCode:
#    Command_IO.run_file_sequence("seq0.txt")
    status = Command_IO.run_file_sequence("blink.txt")
    if (status != Sys_err.ErrorCode.OK):
        return status
    status = Command_IO.run_file_sequence("wink.txt")
    if (status != Sys_err.ErrorCode.OK):
        return status
    return status

def blink(number: int, speed: int, time: int) -> Sys_err.ErrorCode:
    for x in range(number):
        Command_IO.Execute_servo_cmd(Command_IO.Joints.LEFT_EYE_LID, 
                                    Command_IO.servo_data[Command_IO.Joints.LEFT_EYE_LID][2],
                                    speed,
                                    False)
        Command_IO.Execute_servo_cmd(Command_IO.Joints.RIGHT_EYE_LID, 
                                    Command_IO.servo_data[Command_IO.Joints.RIGHT_EYE_LID][2],
                                    speed,
                                    False)
        time.sleep(time * 0.1)
        Command_IO.Execute_servo_cmd(Command_IO.Joints.LEFT_EYE_LID, 
                                    Command_IO.servo_data[Command_IO.Joints.LEFT_EYE_LID][3],
                                    speed,
                                    False)
        Command_IO.Execute_servo_cmd(Command_IO.Joints.RIGHT_EYE_LID, 
                                    Command_IO.servo_data[Command_IO.Joints.RIGHT_EYE_LID][3],
                                    speed,
                                    False)

def wink (number: int, left: bool, sound: bool) -> Sys_err.ErrorCode:
    pass

