#
import sys
import random
import time
import playsound
import pyttsx3

from command_IO import  *
from globals    import  *
#from Sequences  import  *
from playsound import playsound

PI_HEAD_COM_PORT = "com3"
PI_HEAD_BAUD_RATE = 115200
intro_string = "Hello"

Platform_test = Platform_test

command_IO = command_IO()
engine = pyttsx3.init()

# ===========================================================================
# main class

class Pi_the_robot:

    def __init__(self, parent=None):
        serial_port = PI_HEAD_COM_PORT
        serial_baud_rate = PI_HEAD_BAUD_RATE
        voices = engine.getProperty('voices')  # getting details of current voice
        engine.setProperty('voice', voices[1].id)
        engine.say(intro_string)
        engine.runAndWait()
        status = command_IO.open_port(serial_port, serial_baud_rate)
        if ( status !=  ErrorCode.OK):
            print("Fail to open port")
            time.sleep(3)
            sys.exit()


# ===========================================================================
# Main call
#
def main():
    Pi_the_robot()
    print("Hello")

if __name__ == "__main__":
    sys.exit(main())
