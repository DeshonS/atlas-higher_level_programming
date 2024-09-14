#!/usr/bin/python3
"""is_same_class - returns True for same class, False if not"""


def is_same_class(obj, a_class):
    """init is_same_class"""
    if type(obj) is a_class:
        return True
    else:
        return False
