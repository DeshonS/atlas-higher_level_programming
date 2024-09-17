#!/usr/bin/python3
"""load_from_json_file - loads an object from a JSON file"""


import json


def load_from_json_file(filename):
    """init load_from_json_file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
