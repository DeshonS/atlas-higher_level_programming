#!/usr/bin/python3
"""safe_print_division"""


def safe_print_division(a, b):
    """initialize safe_print_division"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
