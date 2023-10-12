#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary.get(key) != None:
        a_dictionary.update(key, value)
    else:
        a_dictionary[key] = value
