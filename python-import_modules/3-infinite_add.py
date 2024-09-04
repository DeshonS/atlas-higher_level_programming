#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    for i in argv[1:]:
        print("{}".format(sum(int(i))))
