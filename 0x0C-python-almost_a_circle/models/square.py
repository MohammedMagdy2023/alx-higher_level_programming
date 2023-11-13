#!/usr/bin/python3
"""
Class Square inherits from Class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square module
    """

    def __init__(self):
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
        super().__init__()
