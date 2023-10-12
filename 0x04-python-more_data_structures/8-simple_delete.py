#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    KEY_ERROR = a_dictionary.get(key, 1)
    if KEY_ERROR != 1:
        del a_dictionary[key]
    return a_dictionary
