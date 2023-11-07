#!/usr/bin/python3
"""Defines class BaseGeometry."""


class BaseGeometry:
    """Reprsent class BaseGeometry."""

    def area(self):
        """No implement till now."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a value as an integer.

        Arguments:
            name: The name of the parameter.
            value: The parameter to validate.
        Errors:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
