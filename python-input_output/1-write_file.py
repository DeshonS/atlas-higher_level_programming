#!/usr/bin/python3
"""write_file - writes text to a file"""


def write_file(filename="", text=""):
    """init write_file"""
    with open(filename, 'w', encoding='utf-8') as file:
        return (f.write(text))
