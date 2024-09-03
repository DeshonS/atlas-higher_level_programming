#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 1:
        print("{:d} {:s}:".format(num, "argument"))
    elif length > 1:
        print("{:d} {:s}:".format(num, "arguments"))
    else:
        print("{:d} {:s}.".format(num, "arguments"))

    for i, j in enumerate(argv):
        if i > 0:
            print("{}: {}".format(i, j))
