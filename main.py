#
import sys
import time

import Pi_the_robot

from Command_IO   import  ErrorCode
from Pi_sound     import  *
from Globals      import  *
from Constants    import  *

# ===========================================================================
# Main call
#
def main():
    if (len(sys.argv) < 2):
        status = Pi_the_robot.init_sys(Sys_strings.PI_HEAD_COM_PORT)
    else:
        status = Pi_the_robot.init_sys(sys.argv[1])
    if (status != ErrorCode.OK):
        Pi_the_robot.sys_print(status)
        pass   # need a way to show error
    play_TTS_string(Sys_strings.INTRO_STRING, True)
    Pi_the_robot.sys_print("Hello")
    Pi_the_robot.run_sys()

if __name__ == "__main__":
    sys.exit(main())
