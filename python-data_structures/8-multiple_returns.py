#!/usr/bin/python3
def multiple_return(sentence):
    length = len(sentence)
    if length > 0:
        i = sentence[0]
    else:
        i = "None"
    new = length, i
    return (new)
