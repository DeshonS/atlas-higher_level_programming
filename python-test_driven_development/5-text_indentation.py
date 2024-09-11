#!/usr/bin/python3
"""separates strings to new lines based on certain symbols"""


def text_indentation(text):
    """init text_indentation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result.strip(), end="")
