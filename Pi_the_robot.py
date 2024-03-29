
#
# Module : Pi_the_robot
#
import Command_IO

from Globals    import  *
from Constants  import  *
from Pi_sound   import  *

# ===========================================================================

    #def __init__(self):
        # serial_port = Sys_strings.PI_HEAD_COM_PORT
        # serial_baud_rate = Sys_values.PI_HEAD_BAUD_RATE
        # voices = engine.getProperty('voices')  # getting details of current voice
        # engine.setProperty('voice', voices[1].id)
        # engine.say(Sys_strings.INTRO_STRING)
        # engine.runAndWait()
        
def init_sys():
    Command_IO.command_IO_init()
    # status = Command_IO.open_port(Sys_strings.PI_HEAD_COM_PORT, Sys_values.PI_HEAD_BAUD_RATE)
    # if ( status !=  Command_IO.close_portErrorCode.OK):
    #     print("Fail to open port")
    #     return status
    # status = Command_IO.ping()
    # if ( status !=  Command_IO.ErrorCode.OK):
    #     print("Fail to Ping board")
    #     return status
    init_sound_output()
    return Command_IO.ErrorCode.OK

