
#
# Module : Pi_the_robot
#
import Command_IO

from Globals    import  *
from Constants  import  *
from Pi_sound   import  *
from Sequences  import  *

# ===========================================================================
        
def init_sys(comport):
    Command_IO.command_IO_init()
    if (Sys_values.TEST_MODE == False):
        status = Command_IO.open_port(Sys_strings.PI_HEAD_COM_PORT, Sys_values.PI_HEAD_BAUD_RATE)
        if ( status !=  Command_IO.ErrorCode.OK):
            sys_print("Fail to open port")
            return status
        status = Command_IO.ping()
        if ( status !=  Command_IO.ErrorCode.OK):
            sys_print("Fail to Ping board")
            return status
    init_sound_output()
    return Command_IO.ErrorCode.OK
#
# print if in debug mode
#
def sys_print(*args):
    if (Sys_values.DEBUG_MODE == True):
        #Iterate over all args, convert them to str, and join them
        args_str = ','.join(map(str,args))
        print(args_str)

def run_sys():
    Command_IO.run_sequence(sequence0)

