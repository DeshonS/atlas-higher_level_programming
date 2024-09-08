#!/usr/bin/python3
"""
square class with value defining size that returns area
"""


class Square:
    """
    initializing class square
    """
    def __init__(self, size=0):
        """initialization"""
        self.size = size

    def size(self):
        """defining variable size"""
        return(self.__size)

    def size(self, value):
        """assigns a value to size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns area of size"""
        return self.__size**2
