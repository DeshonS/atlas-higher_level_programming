#!/usr/bin/python3
"""
class BaseGeometry with modules

area(self) - returns an exception error

integer_validator - sets a value to a given variable name
"""


class BaseGeometry:
    """init class"""
    def area(self):
        """init area(self)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """init integer_validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """init class Rectangle with inheitance"""
    def __init__(self, width, height):
        """init"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """init class Square"""
    def __init__(self, size):
        """init"""
        Rectangle.__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area square"""
        return self.__size * self.__size
