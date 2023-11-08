#!/usr/bin/python3
"""class to json"""


class Student:
    """
    class Student that defines a student by:
    """
    def __init__(self, first_name, last_name, age):
        """
        Public instance attributes:
        Arguments:
            first_name: The first name of the student.
            last_name : The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Public method def to_json(self):
        that retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
