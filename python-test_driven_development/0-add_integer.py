#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is not int or float:
        raise TypeError("a must be an integer")
    if type(b) is not int or float:
        raise TypeError("b must be an integer")
    else:
        total = a + b
        return (total)
