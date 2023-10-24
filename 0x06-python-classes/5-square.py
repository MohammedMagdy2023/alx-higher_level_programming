#!/usr/bin/python3
"""Square Class Startes here"""


class Square:
    """Write a class Square that defines a square by:
    (based on 4-square.py)
    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method:area(self): that returns the current square area
    Public instance method:my_print(self): that prints in stdout the square
    with the character #:
    if size is equal to 0, print an empty line
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        elif value < 0:
            raise "size must be >= 0"
        elif TypeError:
            raise "size must be an integer"

    def area(self):
        return self.__size ** 2 

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
