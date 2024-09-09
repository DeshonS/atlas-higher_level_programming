#!/usr/bin/python3
"""add_integer - function that adds two given numbers together and returns the result"""


def add_integer(a, b=98):
    """defining function name add_integer"""
    if type(a) is not int or float:
        raise TypeError("a must be an integer")
    if type(b) is not int or float:
        raise TypeError("b must be an integer")
    else:
        return (a + b)
