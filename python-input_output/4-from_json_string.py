#!/usr/bin/python3
"""from_json_string - returns an object represented by a JSON string"""


import json


def from_json_string(my_str):
    """init from_json_string"""
    return json.loads(my_str)