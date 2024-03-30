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
    Pi_the_robot.init_sys(sys.argv[1])
    play_TTS_string(Sys_strings.INTRO_STRING, True)
    print("Hello")
    time.sleep(5)

if __name__ == "__main__":
    sys.exit(main())
