#!/usr/bin/python3
"""write a json string into a file"""
import json


def save_to_json_file(my_obj, filename):
    """write a json string into a file"""
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
