#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”:"""
import json


def load_from_json_file(filename):
    """Create object from a JSON file"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
