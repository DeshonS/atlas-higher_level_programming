#!/usr/bin/python3
"""class Square"""
class Square:
    """creating square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization of variables size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size msut be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self__position = value

    def area(self):
        """returns the area of size"""
        return (self.__size**2)

    def my_print(self):
        """prints the square based on size and position"""
        if self.size is 0:
            print()
        else:
            x, y = self.position
            for line in range(y):
                print()
            for line in range(self.size):
                print(" " * x, end="")
                print("#" * self.size)

