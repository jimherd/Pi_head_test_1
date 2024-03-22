#
import sys
import serial
import serial.tools.list_ports
import random
import time
#import pyttsx3
#from playsound import playsound

from command_IO import  *
#from Globals    import  *
#from Sequences  import  *
#from Sound_out  import  *

# ===========================================================================
# main class

class Pi_the_robot:
    command_IO = command_IO()
#    Sound_out  = Sound_out()

    def __init__(self, parent=None):
        ports = list(serial.tools.list_ports.comports())
        if (len(ports) == 0):
            print("No serial ports on system")
            sys.exit()

# ===========================================================================
# Main call
#
def main():
    app = Pi_the_robot()
    print("Hello")

if __name__ == "__main__":
    sys.exit(main())
