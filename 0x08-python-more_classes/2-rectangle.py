#!/usr/bin/python3
"""
A rectangle with width and height.
"""


class Rectangle:
    """
    Defined class Rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initialization of rect and args
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get/set for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Get/set for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get/set for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Get/set for height
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
