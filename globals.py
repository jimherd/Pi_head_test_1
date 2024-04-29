# This Python file uses the following encoding: utf-8

# note :  ._name is the convention to indicate non-public attributes

import platform

from Constants    import  *

from enum import Enum, IntEnum


class Platform_test():
    def __init__(self):
        self._current_platform = This_platform.UNKNOWN
        self._current_platform_name = ""

    def check_platform(self):
        self._current_platform_name = platform.system()
        if (self._current_platform_name == "Windows"):
            self._current_platform = This_platform.WINDOWS
        if (self._current_platform_name == "Linux"):
            self._current_platform = This_platform.LINUX

    def get_platform(self):
        return self._current_platform

    def get_platform_name(self):
        return self._current_platform_name

