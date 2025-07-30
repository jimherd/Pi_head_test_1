#
# Module : Pi_the_robot
#
import time

import Command_IO 
import Messages
import Pi_sound
import Pi_the_robot
import display

from Globals    import  *
from Constants  import  *

from Sequences  import  *

import asyncio


# ===========================================================================

def sys_print(*args) -> None:
    """
    Prints the given arguments to the console if DEBUG_MODE is enabled.

    This function takes a variable number of arguments, converts each argument to a string,
    joins them with a comma separator, and prints the resulting string to the console.
    The printing only occurs if the DEBUG_MODE flag in the Sys_values module is set to True.

    Args:
        *args: Variable number of arguments to be printed. Each argument will be converted to a string.

    Returns:
        None
    """
    if (Sys_values.DEBUG_MODE == True):
        #Iterate over all args, convert them to str, and join them
        args_str = ','.join(map(str,args))
        print(args_str)

# ===========================================================================
def speak_message(err_code: Messages.MessageCode) -> None:
    """
    Plays a TTS (Text-to-Speech) string based on the given message code.

    This function retrieves the message string associated with the provided error code
    from the `Message_string_dict` in the `Messages` module and uses it as input
    for the `play_TTS_string` function. The TTS string is then played.

    Args:
        err_code (Messages.MessageCode): The message code representing the string to be spoken.

    Returns:
        None
    """
    Pi_sound.say_espeak(Messages.Message_string_dict[err_code])

# ===========================================================================
def run_sys() -> Messages.MessageCode:
    
    """
    Runs a sequence of commands to control the robot's actions.

    This function executes a series of commands It checks the status after each command
    and returns an error code if any of the commabd fails.

    Returns:
        Messages.MessageCode: The status code indicating the success or failure of the sequence execution.
                              Returns the error code if any sequence fails; otherwise, returns the status of the last executed sequence.
    """
#    Command_IO.run_file_sequence("seq0.txt")
    status = Command_IO.run_file_sequence("blink.txt")
    if (status != Messages.MessageCode.OK):
        return status
    status = Command_IO.run_file_sequence("wink.txt")
    if (status != Messages.MessageCode.OK):
        return status
    return status

# ===========================================================================
def blink(number: int, speed: int, time: int) -> Messages.MessageCode:
    """
    Controls the robot's eyes to blink a specified number of times.

    This function sends commands to the robot's head to simulate blinking. It moves both the left and right eye lids
    a certain number of times, with a specified speed, and a delay between each blink.

    Args:
        number (int): The number of times the robot should blink.
        speed (int): The speed at which the eyelids move.
        time (int): The duration of the pause between closing and opening the eyelids, in milliseconds.

    Returns:
        Messages.MessageCode: Returns a status code, but the function does not currently check or return any specific error codes.
    """
    for x in range(number):
        Command_IO.Execute_servo_cmd(Command_IO.Joints.LEFT_EYE_LID, 
                                    Command_IO.servo_data[Command_IO.Joints.LEFT_EYE_LID][2],
                                    speed,
                                    False)
        Command_IO.Execute_servo_cmd(Command_IO.Joints.RIGHT_EYE_LID, 
                                    Command_IO.servo_data[Command_IO.Joints.RIGHT_EYE_LID][2],
                                    speed,
                                    False)
        time.sleep(time * 0.1)
        Command_IO.Execute_servo_cmd(Command_IO.Joints.LEFT_EYE_LID, 
                                    Command_IO.servo_data[Command_IO.Joints.LEFT_EYE_LID][3],
                                    speed,
                                    False)
        Command_IO.Execute_servo_cmd(Command_IO.Joints.RIGHT_EYE_LID, 
                                    Command_IO.servo_data[Command_IO.Joints.RIGHT_EYE_LID][3],
                                    speed,
                                    False)

def wink (number: int, left: bool, sound: bool) -> Messages.MessageCode:
    pass

# ===========================================================================
def run_display_test() -> None:
    for i in range(4):
        display.set_display_contrast(10)
        time.sleep(2)
        display.set_display_contrast(90)
        time.sleep(2)

    display.set_display_form(1)
    time.sleep(5)
    display.set_display_form(0)
    return Messages.MessageCode.OK

