# This Python file uses the following encoding: utf-8

# note :  ._name is the convention to indicate non-public attributes

import platform

from Constants    import  *

from enum import Enum, IntEnum

current_platform_name = ""
current_platform = This_platform.UNKNOWN

def check_platform() -> None:
    current_platform_name = platform.system()
    if (current_platform_name == "Windows"):
        current_platform = This_platform.WINDOWS
    if (current_platform_name == "Linux"):
        current_platform = This_platform.LINUX

def get_platform():
    return current_platform

def get_platform_name():
    return current_platform_name

