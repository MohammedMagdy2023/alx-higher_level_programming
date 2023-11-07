#!/usr/bin/python3
"""a function that returns True if the object is an instance of
a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
Prototype: def inherits_from(obj, a_class):
"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
