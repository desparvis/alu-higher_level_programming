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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
