#!/usr/bin/python3
"""from json to obj"""
import json


def from_json_string(my_str):
    """Json load into obj"""
    return json.loads(my_str)
