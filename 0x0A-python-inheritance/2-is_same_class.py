#!/usr/bin/python3
"""
a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
Prototype: def is_same_class(obj, a_class):
"""


def is_same_class(obj, a_class):
    """This function uses the type() function
    to get the exact class of the object,
    and then compares it with a_class
    """
    return type(obj) is a_class
