#!/usr/bin/python3
"""reads a file"""


def read_file(filename=""):
    """init read_file"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
