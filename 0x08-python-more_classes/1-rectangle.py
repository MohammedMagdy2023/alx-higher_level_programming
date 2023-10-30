#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Getters and Setters"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__hieght = height

    @property  # getter
    def width(self):
        return self.__width

    @property  # getter
    def height(self):
        return self.__hieght

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__hieght = value
