#!/usr/bin/python3
def print_tebahpla():
    for i in range(26):
        print("{}".format("".join(chr(122 - i + 32 * (i % 2)))), end="")
        