#!/usr/bin/python3
"""
Class Square inherits from Class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square module
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        The init of the new class instances
        Args:
            size: The size of the new square.
            x: The x of the new Square.
            y: The y of the new Square.
            id: The id of the new Square.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """The size Private instance getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """The size Private instance setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __str__(self):
        """return the string representation of the class"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
