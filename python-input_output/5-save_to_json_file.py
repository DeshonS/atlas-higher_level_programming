#!/usr/bin/python3
"""save_to_json_file - writes an object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """init save_to_json"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
