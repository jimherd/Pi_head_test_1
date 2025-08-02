# This Python file uses the following encoding: utf-8

# note :  ._name is the convention to indicate non-public attributes

import platform
import serial.tools.list_ports

#from Constants    import  *
import Constants
#import Messages

# from enum import Enum, IntEnum

current_platform_name = ""
current_platform = Constants.This_platform.UNKNOWN

def check_platform() -> None:
    global current_platform_name, current_platform
    current_platform_name = platform.system()
    if (current_platform_name == "Windows"):
        current_platform = Constants.This_platform.WINDOWS
    if (current_platform_name == "Linux"):
        current_platform = Constants.This_platform.LINUX

def get_platform():
    return current_platform

def get_platform_name() -> str:
    return current_platform_name

FTDI_VID     = 0x403
FTDI_232_PID = 0x6015

def get_COM_port(the_platform : Constants.This_platform) -> str:
    if (the_platform == Constants.This_platform.LINUX):
        return Constants.Sys_strings.PI_COM_PORT
    if (the_platform == Constants.This_platform.WINDOWS):
        for port in serial.tools.list_ports.comports():
            if ((port.vid == FTDI_VID) and (port.pid == FTDI_232_PID)):
                return port.name
        return "None"
    return 
