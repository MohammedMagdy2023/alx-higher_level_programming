#!/usr/bin/python3
"""The base class is here"""
import json
import csv

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
        with open(cls.__name__ + ".json", "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instantied from a dictionary of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_class = cls(1, 1)
            else:
                new_class = cls(1)
            new_class.update(**dictionary)
            return new_class

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of JSON strings.
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                dicts = Base.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        write a csv file of list_objs
        """
        with open(cls.__name__ + '.csv', 'w', newline='') as f:
            if list_objs is not None:
                writer = csv.writer(f)
                if cls.__name__ == 'Rectangle':
                    writer.writerow(['id', 'width', 'height', 'x', 'y'])
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    writer.writerow(['id', 'size', 'x', 'y'])
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a file of csv strings.
        """
        try:
            with open(cls.__name__ + '.csv', 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        id, width, height, x, y = row
                        cls.__name__.append(cls(int(width), int(height), int(x), int(y), int(id)))
                    elif cls.__name__ == 'Square':
                        id, size, x, y = row
                        cls.__name__.append(cls(int(size), int(x), int(y), int(id)))
        except IOError:
            return []
