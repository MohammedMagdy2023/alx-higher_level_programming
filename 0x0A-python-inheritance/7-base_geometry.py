#!/usr/bin/python3
"""Empty class BaseGeometry"""


class BaseGeometry:
    """implement area function and integer_validator"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an integer".format(name))
