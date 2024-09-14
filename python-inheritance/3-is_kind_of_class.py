#!/usr/bin/python3
"""checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """init is_kind_of_class"""
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
