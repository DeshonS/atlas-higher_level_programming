#!/usr/bin/python3
"""class student that defines a student"""


class Student:
    """init class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """init to_json"""
        if attrs is None:
            return self.__dict__
        new = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new[key] = value
        return new

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
