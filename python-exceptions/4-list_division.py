#!/usr/bin/python3
"""list_division - divides items in two lists"""


def list_division(my_list_1, my_list_2, list_length):
    """init list_division"""
    new_list = []

    for i in range(list_length):
        try:
            # Try to divide corresponding elements of the two lists
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)

    return new_list
