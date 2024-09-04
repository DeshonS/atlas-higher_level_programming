#!/usr/bin/python3
def best_score(a_dictionary):
    value = 0
    for i in a_dictionary:
        if i > value:
            value = i
    return value
