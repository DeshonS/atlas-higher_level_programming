#!/usr/bin/python3
"""square class"""


class Square:
    def __init__(self, size=0):
        """defining size and conditions
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """defining area function
        """
        return(self.__size**2)
