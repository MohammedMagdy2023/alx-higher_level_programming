#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Getters and Setters"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Arguments:
            width: The width of the rectangle.
            height: The height of the rectangle.
        Errors:
            width and height should be integer or exception raised
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2
