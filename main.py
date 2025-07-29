#
import sys
import time

import Pi_the_robot
import Command_IO
import Globals
import asyncio
import IMX500_sys
import Pi_sound
#import TTS


import Messages
#from Pi_sound     import  *
from Constants    import  *
from IMX500_sys   import  *

import cv2
import numpy as np
from functools import lru_cache

# ===========================================================================
# Main call
#
def main():
    #init_sound_output()
    imx500_init()
    Pi_sound.say_espeak("Hello, I am Pi the robot. I am ready to help you.")

    # run_detect()    # temp test

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
    Pi_sound.say_espeak(Sys_strings.INTRO_STRING)

    Pi_the_robot.sys_print("Hello")
    Pi_the_robot.run_display_test()
    Pi_the_robot.run_sys()
    

if __name__ == "__main__":
    sys.exit(main())
