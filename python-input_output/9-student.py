#!/usr/bin/python3
"""class student that defines a student"""


class Student:
    """init class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """init to_json"""
        return self.__dict__
