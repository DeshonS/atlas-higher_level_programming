#!/usr/bin/python3
"""class_to_json - returns dictionary description with data struct"""


def class_to_json(obj):
    """init class_to_json"""
    return vars(obj)
