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
        """The width Private instance getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """The width Private instance setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height Private instance getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """The height Private instance setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x Private instance getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """The x Private instance setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y Private instance getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """The y Private instance setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """print the width and height of the Rectangle as # """
        if self.width == 0 or self.height == 0:
            print("")
            return
        else:
            for _ in range(self.y):
                print("")
            for _ in range(self.height):
                for _ in range(self.x):
                    print(" ", end="")
                for _ in range(self.width):
                    print("#", end="")
                print()

    def __str__(self):
        """return the string representation of the class"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument is the id attribute
                - 2nd argument is the width attribute
                - 3rd argument is the height attribute
                - 4th argument is the x attribute
                - 5th argument is the y attribute
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
