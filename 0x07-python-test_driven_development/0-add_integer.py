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

    c_a = isinstance(a, int) or isinstance(a, float)
    c_b = isinstance(b, int) or isinstance(b, float)
    if c_a and c_b:
        return int(a) + int(b)
    else:
        if not c_a and not c_b:
            raise TypeError("a and b must be integers or floats")
        elif not c_a:
            raise TypeError("a must be an integer")
        elif not c_b:
            raise TypeError("b must be an integer")
        else:
            Exception("Unkown Error happened")
