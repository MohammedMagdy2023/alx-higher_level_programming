#!/usr/bin/python3
"""The base class is here"""


class Base:
    """
    the first base class
    private attr __nb_objects
    """


    __nb_objects = 0

    def __init__(self, id=None):
        """
        the class constructor

        Arguments
        id: the id of the class to prevent dublications
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
