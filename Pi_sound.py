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

import Messsages

from playsound  import  *
# import Command_IO
# from Command_IO import  MessageCode
from Globals    import  *
from Constants  import  *

_sound_dir = os.path.join(os.getcwd(), "Media", "Sounds")
__engine = pyttsx3.init()

def init_sound_output():
    voices = __engine.getProperty('voices')  # getting details of current voice
    __engine.setProperty('voice', voices[1].id)
    print(f"sound_dir = {_sound_dir}")

def play_sound_file(filename: str, block: bool) -> Messsages.MessageCode:
    file = os.path.join(_sound_dir, filename)
    if os.path.isfile(file):
        playsound(file, block)
        return Messsages.MessageCode.OK
    return Messsages.MessageCode.FILE_NOT_FOUND
    

def play_TTS_string(sentence, block):
    __engine.say(sentence)
    if (block == True):
        __engine.runAndWait()

def TTS_wait_finish():
    while (__engine.isBusy == True):
        time.sleep(0.1)



