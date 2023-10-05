#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_c = len(sys.argv) - 1
    if arg_c == 1:
        print("1 argument:")
    elif arg_c == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(arg_c))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
