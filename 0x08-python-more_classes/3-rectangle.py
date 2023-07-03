#!/usr/bin/python3
""" Class Rectangle """


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

    @property
    def height(self):
        """ Get/set for height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ Get/set for width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ Get/set for height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Return area of rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Return perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ Return string to print rectangle with # """
        if self.width == 0 or self.height == 0:
            return ''
        to_print = ''
        for col in range(self.height):
            for row in range(self.width):
                to_print += '#'
            if col != self.height - 1:
                to_print += '\n'
        return to_print
