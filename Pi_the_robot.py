#
# Module : Pi_the_robot
#
import time

import Command_IO as Cmd
import Messages
import Pi_sound
import display
import Constants as Cnst


# ===========================================================================
# glibal variables
# ===========================================================================

current_form = Cnst.forms.FORM_0
press_time   = 0

#
# Dictionary to hold system test results
#
test_results = {
    "left_eye" : {
        "up_down"   : 0,
        "left_right": 0,
        "lid"       : 0,
        "brow"      : 0
    },
    "right_eye" : {
        "up_down"   : 0,
        "left_right": 0,
        "lid"       : 0,
        "brow"      : 0
    },
    "head" : {
        "mouth"     : 0,
        "neck"      : 0,
    },
    "lights" : {
        "neopixels" : 0,
  }
} 


# ===========================================================================

def sys_print(*args) -> None:
    """
    Prints the given arguments to the console if DEBUG_MODE is enabled.

    This function takes a variable number of arguments, converts each argument to a string,
    joins them with a comma separator, and prints the resulting string to the console.
    The printing only occurs if the DEBUG_MODE flag in the Sys_values module is set to True.

    Args:
        *args: Variable number of arguments to be printed. Each argument will be converted 
               to a string.

    Returns:
        None
    """
    if (Cnst.Sys_values.DEBUG_MODE == True):
        #Iterate over all args, convert them to str, and join them (space separator)
        args_str = ' '.join(map(str,args))
        print(args_str)

# ================================================
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
        Messages.MessageCode: The status code indicating the success or failure of the 
        sequence execution. Returns the error code if any sequence fails; otherwise, 
        returns the status of the last executed sequence.
    """
#    Command_IO.run_file_sequence("seq0.txt")
    status = Cmd.run_file_sequence("blink.txt")
    if (status != Messages.MessageCode.OK):
        return status
    status = Cmd.run_file_sequence("wink.txt")
    if (status != Messages.MessageCode.OK):
        return status
    return status

# ===========================================================================
def blink(number: int, speed: int, dwell_time: int) -> Messages.MessageCode:
    """
    Controls the robot's eyes to blink a specified number of times.

    This function sends commands to the robot's head to simulate blinking. 
    It moves both the left and right eye lids a certain number of times, 
    with a specified speed, and a delay between each blink.

    Args:
        number (int): The number of times the robot should blink.
        speed (int): The speed at which the eyelids move.
        time (int): The duration of the pause between closing and opening the 
        eyelids, in milliseconds.

    Returns:
        Messages.MessageCode: Returns a status code, but the function does not 
        currently check or return any specific error codes.
    """
    for _ in range(number):
        Cmd.Execute_servo_cmd(Cmd.Joints.LEFT_EYE_LID,
                                    Cmd.servo_data[Cmd.Joints.LEFT_EYE_LID][2],
                                    speed,
                                    False)
        Cmd.Execute_servo_cmd(Cmd.Joints.RIGHT_EYE_LID, 
                                    Cmd.servo_data[Cmd.Joints.RIGHT_EYE_LID][2],
                                    speed,
                                    False)
        time.sleep(dwell_time * 0.1)
        Cmd.Execute_servo_cmd(Cmd.Joints.LEFT_EYE_LID,
                                    Cmd.servo_data[Cmd.Joints.LEFT_EYE_LID][3],
                                    speed,
                                    False)
        Cmd.Execute_servo_cmd(Cmd.Joints.RIGHT_EYE_LID,
                                    Cmd.servo_data[Cmd.Joints.RIGHT_EYE_LID][3],
                                    speed,
                                    False)

# def wink (number: int, left: bool, sound: bool) -> Messages.MessageCode:
#     pass

# ===========================================================================
def run_display_test() -> Messages.MessageCode:
    for _ in range(4):
        status = display.set_display_contrast(10)
        if (status != Messages.MessageCode.OK): 
            return status
        time.sleep(2)
        status = display.set_display_contrast(90)
        if (status != Messages.MessageCode.OK): 
            return status
        time.sleep(2)

    status = display.set_display_form(1)
    if (status != Messages.MessageCode.OK):
        return status
    time.sleep(5)
    status = display.set_display_form(0)
    if (status != Messages.MessageCode.OK): 
        return status
    status = display.set_display_contrast(10)
    if (status != Messages.MessageCode.OK): 
        return status

    return Messages.MessageCode.OK

# ===========================================================================
def run_program() -> Messages.MessageCode:
    global current_form, press_time

    status = display.set_display_form(Cnst.forms.FORM_0)
    if (status != Messages.MessageCode.OK): 
        return status
    current_form = Cnst.forms.FORM_0

    # Main SYSTEM loop
    #       1. scan buttons on current form. 
    #       2. Use pressed button 'local index' to call form action
    #       3. repeat
    #
    # Notes
    #       a. 'local index' of pressed button returned in 'int_parameter[2]'
    #       b. Length of press returned in 'int_parameter[3]

    while True:
        status = display.scan_uLCD_form_for_button_presses(current_form, 0)
        if (status != Messages.MessageCode.OK): 
            return status
        local_id = Cmd.int_parameter[2]
        press_time = Cmd.int_parameter[3]   

        match current_form:
            case Cnst.forms.FORM_0:                 # Power-on FORM
                status = form_0_actions(local_id)
                if status != Messages.MessageCode.OK:
                    return status
            case Cnst.forms.FORM_1:                 # Test LEFT eye FORM
                status = form_1_actions(local_id)
                if status != Messages.MessageCode.OK:
                    return status
            case Cnst.forms.FORM_2:                 # Test RIGHT eye FORM
                status = form_2_actions(local_id)
                if status != Messages.MessageCode.OK:
                    return status
                pass

# ===========================================================================
def run_left_eye_tests() -> Messages.MessageCode:
    for _ in range(5):
        status = Cmd.run_file_sequence("left_eye_tests.txt")
        if (status != Messages.MessageCode.OK):
            break
    # read test switches
    test_results["left_eye"]["up_down"] = 1
    return status

# ===========================================================================
def run_right_eye_tests() -> Messages.MessageCode:
    for _ in range(5):
        status = Cmd.run_file_sequence("right_eye_tests.txt")
        if (status != Messages.MessageCode.OK):
            return status
    return status

# ===========================================================================
def form_0_actions(local_index: int) -> Messages.MessageCode:
    global current_form

    while True:
        match local_index:
            case Cnst.button_id.buttton_id_0:
                status = display.set_display_form(Cnst.forms.FORM_0)
                if (status != Messages.MessageCode.OK): 
                    return status
            case Cnst.button_id.buttton_id_1:
                status = display.set_display_form(Cnst.forms.FORM_1)
                if (status != Messages.MessageCode.OK): 
                    return status
                current_form = Cnst.forms.FORM_1
            case _:
                time.sleep(0.5)    # delay for half second
                return Messages.MessageCode.NO_BUTTON_PRESSED

# ===========================================================================
def form_1_actions(local_index: int) -> Messages.MessageCode:
    global current_form

    while True:
        match local_index:
            case Cnst.button_id.buttton_id_0:
                status = run_left_eye_tests() 
            case Cnst.button_id.buttton_id_1:
                status = display.set_display_form(Cnst.forms.FORM_2)
                if (status != Messages.MessageCode.OK): 
                    return status
                current_form = Cnst.forms.FORM_1
            case Cnst.button_id.buttton_id_2:
                status = display.set_display_form(Cnst.forms.FORM_0)
                if (status != Messages.MessageCode.OK): 
                    return status
            case _: 
                time.sleep(0.5)    # delay for half second
                return Messages.MessageCode.NO_BUTTON_PRESSED
            
# ===========================================================================
def form_2_actions(local_index: int) -> Messages.MessageCode:
    global current_form

    while True:
        match local_index:
            case Cnst.button_id.buttton_id_0:
                status = run_right_eye_tests()
            case Cnst.button_id.buttton_id_1:
                status = display.set_display_form(Cnst.forms.FORM_2)
                if (status != Messages.MessageCode.OK): 
                    return status
                current_form = Cnst.forms.FORM_2
            case Cnst.button_id.buttton_id_2:
                status = display.set_display_form(Cnst.forms.FORM_0)
                if (status != Messages.MessageCode.OK): 
                    return status
            case _: 
                time.sleep(0.5)    # delay for half second
                return Messages.MessageCode.NO_BUTTON_PRESSED
    