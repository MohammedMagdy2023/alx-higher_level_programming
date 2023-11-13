#!/usr/bin/python3
"""The Rectangle class that inherit from base class"""
from models.base import Base


class Rectangle(Base):
    """
    The Rectangle Class thaat inherit from base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The init of the new class instances
        Args:
            width: The width of the new Rectangle.
            height: The height of the new Rectangle.
            x: The x of the new Rectangle.
            y: The y of the new Rectangle.
            id: The id of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

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
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(0, self.x):
            print('\n', end="")
        for _ in range(0, self.height):
            for _ in range(0, self.y):
                print(" ", end="")
            for _ in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
                - {self.width}/{self.height}"
