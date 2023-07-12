#!/usr/bin/python3
"""A class that defines a student by attributes, Instantiation and method"""


class Student:
    """student class."""

    def __init__(self, first_name, last_name, age):
        """Student class constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
