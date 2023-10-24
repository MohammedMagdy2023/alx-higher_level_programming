#!/usr/bin/python3
"""Square Class Startes here"""


class Square:
    """Create a class Square that defines a square by
        Private instance attribute: size
        Public instance method: area(self): returns the current square area
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        value = int(self.__size) ** 2
        return value
