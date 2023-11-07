#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of
or if the object is an instance of a class that inherited from
the specified class otherwise False.
Prototype: def is_kind_of_class(obj, a_class):
"""


def is_kind_of_class(obj, a_class):

    """This function uses the isinstance() function
    to get the exact class of the object, 
    and then compares it with a_class
    """
    return isinstance(obj, a_class)
