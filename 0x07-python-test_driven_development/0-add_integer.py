#!/usr/bin/python3
"""
add_integer return the sum of two integer numbers
a and b must be integers or floats, 
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    add_integer return the sum of two integer numbers
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
