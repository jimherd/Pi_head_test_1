#
import sys
import time

import Pi_the_robot
import Command_IO
import Globals

import Messages
from Pi_sound     import  *
from Constants    import  *

# ===========================================================================
# Main call
#
def main():
    init_sound_output()
    Globals.check_platform()
    Command_IO.Pi_head_com_port = Globals.get_COM_port(Globals.get_platform())
    if (Command_IO.Pi_head_com_port == "None"):
        Pi_the_robot.sys_print(Messages.MessageCode.NO_COM_PORT_FOUND)
        Pi_the_robot.speak_message(Messages.MessageCode.NO_COM_PORT_FOUND)
        time.sleep(2)
        return

    if (len(sys.argv) > 1):
        Command_IO.Pi_head_com_port = sys.argv[1]

    status = Command_IO.init_sys(Command_IO.Pi_head_com_port)
    if (status != Messages.MessageCode.OK):
        Pi_the_robot.sys_print(status)
        Pi_the_robot.speak_message(status)
        time.sleep(5)
        return
    play_TTS_string(Sys_strings.INTRO_STRING, True)
    Pi_the_robot.sys_print("Hello")
    Pi_the_robot.run_sys()
    

if __name__ == "__main__":
    sys.exit(main())
