#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        c_value = 0
        for key in a_dictionary.keys():
            if a_dictionary[key] >= c_value:
                c_value = a_dictionary[key]
            return key
            break
