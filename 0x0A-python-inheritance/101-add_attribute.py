#!/usr/bin/python3
"""a function that adds attributes to objects."""


def add_attribute(obj, attr, value):
    """ Add attribute to an object """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
