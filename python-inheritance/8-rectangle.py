#!/usr/bin/python3
"""
define module
"""


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """
    now this class is imported
    """

    def __init__(self, width, height):
        """
        define init brev
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
