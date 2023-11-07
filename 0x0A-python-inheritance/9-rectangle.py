#!/usr/bin/python3
"""a  class Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new instance.

        Args:
            width: The width of the new Rectangle.
            height: The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the representation of a Rectangle class implementation."""
        representation = "[" + str(self.__class__.__name__) + "] "
        representation += str(self.__width) + "/" + str(self.__height)
        return representation
