# This Python file uses the following encoding: utf-8
#
# Set of command sequences that can be executed
# Notes
#    * If a command returns an error code then the command sequence is aborted
#
# Sequences
#    0. simple speak/mouth move actions
#    1. Play a sound file mp3/wav on local machine
#    2. Flip pages on display

sequence0 = [   # power on
        "ping 9 40",
        "servo 9 0 8 45",              # mouth ON
        "speak t w Welcome to the Pi the robot system",
        "delay 1",
        "servo 9 0 8 0",              # mouth OFF
        "delay 3",
        "servo 9 0 8 45",              # mouth ON
        "speak f w intro.txt",
        "servo 9 0 8 0",              # mouth OFF
]
sequence1 = [
        "ping 9 42",
        "plays mixkit-classic-alarm-995.wav",
]
sequence2 = [
        "ping 9 42",
        "display 9 0 1",
        "delay 5",
        "display 9 0 0",
]
sequence3 = [
        "ping 9 43",
        "display 9 0 1",
        "display 9 4 0 \"Hello Jim\"",
]
