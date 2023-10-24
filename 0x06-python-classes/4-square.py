#!/usr/bin/python3
"""Square Class Startes here"""


class Square:
    """Create a class Square that defines a square by
        Private instance attribute: size
        Public instance method: area(self): returns the current square area
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        value = int(self.__size) ** 2
        return value
