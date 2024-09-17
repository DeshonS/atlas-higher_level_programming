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
