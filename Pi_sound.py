#
# Module : Implement sound and text-to-speech features
#
# Globals 
#         Name         Scope
#        __engine      module
#        __sound_dir   module

import os
import subprocess
import time
import pyttsx3

import Messages

from playsound  import  *
# import Command_IO
# from Command_IO import  MessageCode
from Globals    import  *
from Constants  import  *

_sound_dir = os.path.join(os.getcwd(), "Media", "Sounds")
__engine = pyttsx3.init()

def init_sound_output():
    # voices = __engine.getProperty('voices')  # getting details of current voice
    # __engine.setProperty('voice', voices[1].id)
    print(f"sound_dir = {_sound_dir}")

def play_sound_file(filename: str, block: bool) -> Messages.MessageCode:
    file = os.path.join(_sound_dir, filename)
    if os.path.isfile(file):
        playsound(file, block)
        return Messages.MessageCode.OK
    return Messages.MessageCode.FILE_NOT_FOUND
    

# def play_TTS_string(sentence, block):
#     __engine.say(sentence)
#     if (block == True):
#         __engine.runAndWait()

# def TTS_wait_finish():
#     while (__engine.isBusy == True):
#         time.sleep(0.1)

def say_espeak(phrase: str, volume: int = 100) -> None:
    """
    Uses the 'espeak-ng' command-line tool to convert text to speech.
    
    Args:
        phrase (str): The text to be spoken.
        volume (int, optional): The volume for speech synthesis (default is 100).
    """
    # phrase = phrase.replace("I'm", "I m")
    # phrase = phrase.replace("'", "")
    # phrase = phrase.replace('"', ' quote ')
    # phrase = phrase.replace('*', "")

    try:
        cmd = f"espeak-ng -s120 -a{volume} -ven+robosoft3 '{phrase}'"
        py3_out = subprocess.check_output(cmd, shell=True)
        print(f"Espeak-ng command : {cmd}")

    except FileNotFoundError:
        print("Error: 'espeak' command not found. Please install it.")
    except subprocess.CalledProcessError as e:
        print(f"Error during speech synthesis: {e}")

def say(phrase: str, volume: int = 150) -> None:
    say_espeak(phrase, volume)

def shout(phrase: str, volume: int = 250) -> None:
    say_espeak(phrase, volume)

def whisper(phrase: str, volume: int = 50) -> None:
    say_espeak(phrase, volume)


