#!/usr/bin/python3
"""print_square - prints a square size"""


def print_square(size):
    """initialize print_square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for row in range(size):
            print('#' * size)
