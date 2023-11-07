#!/usr/bin/python3
"""Load, add, save"""
import sys
save_to_json_file=__import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file=__import__("6-load_from_json_file.py").load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    my_list = load_from_json_file(filename)
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
