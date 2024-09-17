#!/usr/bin/python3
"""add_item - adds all arguments to a Python list and saves to a file"""


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    item_list = load_from_json_file(filename)
except FileNotFoundError:
    item_list = []
items.extend(sys.argv[1:])
save_to_json_file(item_list, filename)
