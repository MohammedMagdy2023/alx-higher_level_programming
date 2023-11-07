#!/usr/bin/python3
"""append into a file"""


def append_write(filename="", text=""):
    """append to a file"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
