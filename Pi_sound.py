#
# Module : Implement sound
#
# Globals 
#         Name         Scope
#        __engine      module

import os
import pyttsx3

from Command_IO import  *
from Globals    import  *
from Constants  import  *

sound_dir = ""

def init_sound_output():
    global __engine 
    __engine = pyttsx3.init()
    voices = __engine.getProperty('voices')  # getting details of current voice
    __engine.setProperty('voice', voices[1].id)

    sound_dir = os.path.join(os.getcwd(), "Media", "Sounds")

def play_sound_file(filename):
    pass

def play_TTS_string(sentence, wait):
    __engine.say(sentence)
    if (wait == True):
        __engine.runAndWait()

