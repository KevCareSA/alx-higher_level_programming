#!/usr/bin/python3
''' A class that defines a student by attributes, Instantiation and method
'''


class Student:
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Student class constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Method that returns dir description '''
        return self.__dict__.copy()
