#!/usr/bin/python3
"""
square class
"""


class Square:
    """
    defining size and errors
    """
    def __init__(self, size=0):
        if size(type) != int:
            print TypeError("size must be an integer")
        if size < 0:
            print ValueError("size must be >= 0")
