#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialization of a new Rectangle."""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
