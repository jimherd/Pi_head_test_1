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

# ===========================================================================
from  Command_IO import *

import Pi_the_robot
import Globals
import Messages
from Constants  import *

# ===========================================================================
# Display functions
# ===========================================================================

def set_display_form(form_index: int) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SET_uLCD_FORM} {form_index}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status

def get_display_form() -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.GET_uLCD_FORM}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status    # current form index is in 'int_parameter[0]'

def set_display_contrast(contrast : int) -> Messages.MessageCode:
    if ((contrast < 0) or (contrast > 100)) :
        return Messages.MessageCode.CONTRAST_OUTWITH_PERCENT_RANGE
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SET_uLCD_CONTRAST} {contrast}\n")
    Pi_the_robot.sys_print(cmd_string)
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status

def read_display_button(form_index : int, local_index : int) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.READ_uLCD_BUTTON}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status    # current button value is in 'int_parameter[0]'

def read_display_switch(form_index : int, local_index : int) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.READ_uLCD_SWITCH}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status   # current switch value is in 'int_parameter[0]'

def read_object(form_index : int, global_index : int, object_type : int) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.READ_uLCD_OBJECT} {global_index} {object_type}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status   # current object value is in 'int_parameter[0]'

def write_display_string(form_index : int, local_index : int, text : str) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.WRITE_uLCD_STRING} {local_index} {text}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status

def write_object(form_index : int, object_type : int, value : int, ) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.READ_uLCD_OBJECT} {object_type} {value}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status

def scan_uLCD_form_for_button_presses(form_index : int) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SCAN_uLCD_FORM_BUTTON_PRESSES} {form_index}\n")
    status =  do_command(cmd_string)
    Pi_the_robot.sys_print(status)
    return status       # local index, and press length in 'int_parameter[]' array