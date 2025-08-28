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

import Command_IO as Cmd

# ===========================================================================
# Display functions
# ===========================================================================

def set_display_form(form_index: int) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SET_uLCD_FORM} {form_index}\n")
    status =  do_command(cmd_string)
    return status

def get_display_form() -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.GET_uLCD_FORM}\n")
    status =  do_command(cmd_string)
    return status    # current form index is in 'int_parameter[0]'

def set_display_contrast(contrast : int) -> Messages.MessageCode:
    if ((contrast < 0) or (contrast > 100)) :
        return Messages.MessageCode.CONTRAST_OUTWITH_PERCENT_RANGE
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SET_uLCD_CONTRAST} {contrast}\n")
    status =  do_command(cmd_string)
    return status   # current object value is in 'int_parameter[0]'

def write_display_string(form_index : int, local_index : int, text : str) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.WRITE_uLCD_STRING} {form_index} {local_index} {text}\n")
    status =  do_command(cmd_string)
    return status

def read_display_button(form_index : int, local_index : int) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.READ_uLCD_BUTTON} {form_index} {local_index}\n")
    status =  do_command(cmd_string)
    return status    # current button value is in 'int_parameter[0]'

def read_display_switch(form_index : int, local_index : int) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.READ_uLCD_SWITCH} {form_index} {local_index}\n")
    status =  do_command(cmd_string)
    return status   # current switch value is in 'int_parameter[0]'

def read_object(object_type : int, global_index : int) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.READ_uLCD_OBJECT} {object_type} {global_index} \n")
    status =  do_command(cmd_string)
    return status   # current object value is in 'int_parameter[0]'

# def write_display_string(form_index : int, local_index : int, text : str) -> Messages.MessageCode:
#     cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.WRITE_uLCD_STRING} {form_index} {local_index} {text}\n")
#     status =  do_command(cmd_string)
#     return status

def write_object(object_type : int, global_index: int, value : int ) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.READ_uLCD_OBJECT} {object_type} {global_index} {value}\n")
    status =  do_command(cmd_string)
    return status

def scan_form_for_button_presses(form_index : int, scans : int = 0) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SCAN_uLCD_BUTTON_PRESSES} {form_index}\n")
    match scans:
        case 0:  # continuous  scan
            while True:
                status =  do_command(cmd_string)
                if (int_parameter[2] == -1):
                    time.sleep(0.5)
                    continue
                else:
                    return status
        case _:
            for _ in range(scans):
                status =  do_command(cmd_string)
                if (int_parameter[2] == -1):
                    time.sleep(0.5)
                    continue
                else:
                    return status
                
def scan_form_switches(form_index: int) -> Messages.MessageCode:
    cmd_string = (f"display {Sys_values.DEFAULT_PORT} {Display_commands.SCAN_uLCD_SWITCHES} {form_index}\n")
    status = do_command(cmd_string)
    
    return status
    
