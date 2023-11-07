#!/usr/bin/python3
"""
a function that returns the list of available attributes and methods:
Prototype: def lookup(obj):
Returns a list object
"""


def lookup(obj):
    """Return the all available methods and attributes"""
    return dir(obj)
