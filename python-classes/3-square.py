#!/usr/bin/python3
class Square:
    """square class"""


    def __init__(self, size=0):
        """initialization

        Args:
            size (int): size of the squares sides

        Raises:
            TypeError: if the size is not an int
            ValueError: if the size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """return the squares area"""
        return (self.__size**2)
