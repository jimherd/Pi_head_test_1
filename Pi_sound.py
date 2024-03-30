#
# Module : Implement sound and text-to-speech features
#
# Globals 
#         Name         Scope
#        __engine      module
#        __sound_dir   module

import os
import pyttsx3

from playsound  import  *
from Command_IO import  *
from Globals    import  *
from Constants  import  *

__sound_dir = ""

def init_sound_output():
    global __engine 
    __engine = pyttsx3.init()
    voices = __engine.getProperty('voices')  # getting details of current voice
    __engine.setProperty('voice', voices[1].id)
    __sound_dir = os.path.join(os.getcwd(), "Media", "Sounds")

def play_sound_file(filename):
    playsound(os.path.join(__sound_dir, filename))

def play_TTS_string(sentence, wait):
    __engine.say(sentence)
    if (wait == True):
        __engine.runAndWait()

