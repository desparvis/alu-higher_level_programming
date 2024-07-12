#!/usr/bin/python3
"""
module and stuff
"""


class Square:
    """
    A class that defines a square with size and position attributes,
    and methods to calculate area and print the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance.

        Args:
        - size (int): Size of the square's side length. Default is 0.
        - position (tuple): Position offset for printing the square. Default is (0, 0).

        Raises:
        - TypeError: If size is not an integer or position is not a tuple of two integers.
        - ValueError: If size is less than 0 or position contains negative integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position."""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters, respecting position offsets."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                spaces = " " * self.__position[0]
                hashes = "#" * self.__size
                print(spaces + hashes)

