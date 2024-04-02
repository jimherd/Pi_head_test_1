#
import sys
import time

import Pi_the_robot
from Pi_sound     import  *
from Globals      import  *
from Constants    import  *

# ===========================================================================
# Main call
#
def main():
    if (len(sys.argv) < 2):
        Pi_the_robot.init_sys(Sys_strings.PI_HEAD_COM_PORT)
    else:
        Pi_the_robot.init_sys(sys.argv[1])
    play_TTS_string(Sys_strings.INTRO_STRING, True)
    print("Hello")
    Pi_the_robot.run_sys()

if __name__ == "__main__":
    sys.exit(main())
