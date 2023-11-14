#!/usr/bin/python3
"""The base class is here"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON of a list of dicts.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write a json file of list_objs"""
        dist = cls.__name__ + ".json"
        with open(dist, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        pass
