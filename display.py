#
# Set of routines to interact with the 4D Systems touch LCD display.
# Commands are sent as ASCII strings to the RP2040 controller to be reformated to
# be sent to the display.  Replys from the display are are partially format as 
# ASCII string to be returned to the Raspberry Pi.  The data from the display
# reply is loaded into the global arrays int_paameter[] and float_parameter[] for 
# further processing.
#
# Details of the ASCII string formats are detailed in the "Commands.docx" file
# in the 'Docs' directory.

from  Command_IO import *

import Pi_the_robot
import Globals
import Messages
from Constants  import *


def set_display_form(page_index) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SET_uLCD_FORM} {page_index}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status

def get_display_form(page_index) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.GET_uLCD_FORM}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status    # current form index is in 'int_parameters[0]'



def read_object() -> Messages.MessageCode:
    """
    Reads an object from the display and returns its status code.

    This function is a placeholder for reading an object from the display.
    It currently returns a status code indicating that the operation is not implemented.

    Returns:
        Messages.MessageCode: A status code indicating that the operation is not implemented.
    """
    return Messages.MessageCode.NOT_IMPLEMENTED
