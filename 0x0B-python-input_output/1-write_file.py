#!/usr/bin/python3
"""Writing into a file"""


def write_file(filename="", text=""):
    """A function that write test to a file and count it"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
