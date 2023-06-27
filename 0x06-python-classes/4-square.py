#!/usr/bin/python3
""" Class Square that defines a square
"""


class Square():
    """square class constructor"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """returns area of square"""
    def area(self):
        return self.__size ** 2

    """getter size"""
    @property
    def size(self):
        return self.__size

    """setter size"""
    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
