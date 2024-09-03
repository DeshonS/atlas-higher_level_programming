#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 129):
            i = chr(ord(i) + (ord("A") - ord("a")))
        print("{:s}".format(i), end="")
    print("")
