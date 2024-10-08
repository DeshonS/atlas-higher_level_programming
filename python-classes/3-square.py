#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """initialization"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size**2)
