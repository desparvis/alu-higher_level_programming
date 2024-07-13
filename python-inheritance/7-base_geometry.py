#!/usr/bin/python3
"""
defining class BaseGeometry
"""


class BaseGeometry:
    """
    this is class
    """
    def area(self):
        """
        raising except and stuff
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validating thing
        """
        if isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
