#
import sys
import time

import Pi_the_robot
import Command_IO
import Globals

import Sys_err
from Pi_sound     import  *
from Constants    import  *

# ===========================================================================
# Main call
#
def main():
    Globals.check_platform()
    if (get_platform() == This_platform.LINUX):
        Command_IO.Pi_head_com_port = Sys_strings.PI_COM_PORT
    else:
        Command_IO.Pi_head_com_port = Sys_strings.WIN_COM_PORT

    if (len(sys.argv) > 1):
        Command_IO.Pi_head_com_port = sys.argv[1]

    status = Command_IO.init_sys(Command_IO.Pi_head_com_port)
    if (status != Sys_err.ErrorCode.OK):
        Pi_the_robot.sys_print(status)
        pass   # need a way to show error
    play_TTS_string(Sys_strings.INTRO_STRING, True)
    Pi_the_robot.sys_print("Hello")
    Pi_the_robot.run_sys()

if __name__ == "__main__":
    sys.exit(main())
