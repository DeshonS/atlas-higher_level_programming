#!/usr/bin/python3
"""Making a square using all of our tools"""


class Square:
    """create class square"""
    def __init__(self, size=0):
        """initialize by assigning size a value"""
        self.size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter to assign size a value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return the area of a square with size valued size"""
        return (self.__size**2)

    def my_print(self):
        """print square"""
        if self.__size is 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print()
