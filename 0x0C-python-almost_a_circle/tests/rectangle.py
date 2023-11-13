#!/usr/bin/python3
"""The Rectangle class that inherit from base class"""


from .base import Base
class Rectangle(Base):
    """
    The Rectangle Class thaat inherit from base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0 :
            raise ValueError("width must be > 0")
        elif not isinstance(value, int):
            raise TypeError("width must be integer")
        else:
            self.__width = value
            return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0 :
            raise ValueError("height must be > 0")
        elif not isinstance(value, int):
            raise TypeError("height must be integer")
        else:
            self.__height= value
            return self.__height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value <= 0 :
            raise ValueError("x must be > 0")
        elif not isinstance(value, int):
            raise TypeError("x must be integer")
        else:
            self.__x = value
            return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value <= 0 :
            raise ValueError("x must be > 0")
        elif not isinstance(value, int):
            raise TypeError("x must be integer")
        else:
            self.__y = value
            return self.__y
