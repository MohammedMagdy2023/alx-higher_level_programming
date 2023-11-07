#!/usr/bin/python3
"""Reading a file"""


def read_file(filename=""):
    """ a function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
