#
# Module : Implement sound and text-to-speech features
#
# Globals 
#         Name         Scope
#        __engine      module
#        __sound_dir   module

import os
import time
import pyttsx3

import Sys_err

from playsound  import  *
# import Command_IO
# from Command_IO import  ErrorCode
from Globals    import  *
from Constants  import  *

_sound_dir = os.path.join(os.getcwd(), "Media", "Sounds")
__engine = pyttsx3.init()

def init_sound_output():
    voices = __engine.getProperty('voices')  # getting details of current voice
    __engine.setProperty('voice', voices[1].id)
    print(f"sound_dir = {_sound_dir}")

def play_sound_file(filename: str, block: bool) -> Sys_err.ErrorCode:
    file = os.path.join(_sound_dir, filename)
    if os.path.isfile(file):
        playsound(file, block)
        return Sys_err.ErrorCode.OK
    return Sys_err.ErrorCode.FILE_NOT_FOUND
    

def play_TTS_string(sentence, block):
    __engine.say(sentence)
    if (block == True):
        __engine.runAndWait()

def TTS_wait_finish():
    while (__engine.isBusy == True):
        time.sleep(0.1)



