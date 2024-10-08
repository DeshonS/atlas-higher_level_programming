#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for b in range(x):
        try:
            print("{:d}".format(my_list[b]), end="")
            i += 1
        except (ValueError, TypeError):
            b += 1
            continue
    print("")
    return i
