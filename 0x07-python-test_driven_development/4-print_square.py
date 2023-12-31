#!/usr/bin/python3
"""
a function that prints a square with the character #
    Prototype: def print_square(size):
"""


def print_square(size):
    """
    size is the size length of the square
    size must be an integer, otherwise
        raise a TypeError exception with the message size must be an integer
    if size is less than 0,
        raise a ValueError exception with the message size must be >= 0
    if size is a float and is less than 0,
        raise a TypeError exception with the message size must be an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        if isinstance(size, int):
            for _ in range(size):
                print("".join("#" * size))
        else:
            raise Exception("Unkown error happend")
