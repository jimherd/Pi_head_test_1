# This Python file uses the following encoding: utf-8

# note :  ._name is the convention to indicate non-public attributes

import platform
import serial.tools.list_ports

from Constants    import  *
import Messages

from enum import Enum, IntEnum

current_platform_name = ""
current_platform = This_platform.UNKNOWN

def check_platform() -> None:
    global current_platform_name, current_platform
    current_platform_name = platform.system()
    if (current_platform_name == "Windows"):
        current_platform = This_platform.WINDOWS
    if (current_platform_name == "Linux"):
        current_platform = This_platform.LINUX

def get_platform():
    return current_platform

def get_platform_name():
    return current_platform_name

FTDI_VID     = 0x403
FTDI_232_PID = 0x6015

def get_COM_port(platform : This_platform):
    if (platform == This_platform.LINUX):
        return Sys_strings.PI_COM_PORT
    if (platform == This_platform.WINDOWS):
        for port in serial.tools.list_ports.comports():
            if ((port.vid == FTDI_VID) and (port.pid == FTDI_232_PID)):
                return port.name
        return "None"
    return 




