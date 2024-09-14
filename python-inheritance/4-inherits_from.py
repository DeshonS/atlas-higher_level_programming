#!/usr/bin/python3
"""returns value if a specified object is an instance of a class"""


def inherits_from(obj, a_class):
    """init inherits_from"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
