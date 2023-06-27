#!/usr/bin/python3
""" Class Square that defines a square
"""


class Square():
    '''New square class constructor'''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """returns area of square"""
    def area(self):
        return self.__size * self.__size
