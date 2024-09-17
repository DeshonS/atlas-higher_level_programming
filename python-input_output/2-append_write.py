#!/usr/bin/python3
"""append_write - appends text to a file"""


def append_write(filename="", text=""):
    """init append_write"""
    with open(filename, 'a', encoding='utf-8') as file:
        return (file.write(text))
