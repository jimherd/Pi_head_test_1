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

sequences = [
    [ # Sequence 0
        "ping 9 40",
        "servo 9 0 8 45",              # mouth ON
        "speak 1 this is a test",
        "delay 1",
        "speak 1 the mouth should be moving",
        "servo 9 0 8 0",              # mouth OFF
    ],
    [ # Sequence 1
    #    "ping 9 42",
        "plays mixkit-classic-alarm-995.wav",
    ],
    [ # Sequence 2
        "ping 9 42",
        "display 9 0 1",
        "delay 5",
        "display 9 0 0",
    ],
    [ # Sequence 3
        "ping 9 43",
        "display 9 0 1",
        "display 9 4 0 \"Hello Jim\"",
    ],
]
