#!/usr/bin/python3
"""a function that returns True if the object is an instance of
a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
Prototype: def inherits_from(obj, a_class)."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Arguments:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Return:
        If obj is an inherited instance of a_class - True.
        If obj isn't an inherited instance of a_class - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
