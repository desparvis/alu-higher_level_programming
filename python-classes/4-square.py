#!/usr/bin/python3
"""
define class
"""


class Square:
    """
    class stuff mens
    """
    def __init__(self, size=0):
        self.size = size
    def size(self):
        return self.__size
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
