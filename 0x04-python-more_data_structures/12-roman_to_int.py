#!/usr/bin/python3
def roman_to_int(roman_string):
    RS = roman_string
    if isinstance(RS, str) or RS is None:
        return 0
    else:
        character = ["I", "V", "X", "L", "C", "D", "M"]
        INTIGER = [1, 5, 10, 50, 100, 500, 1000]
        dict_guid = dict(zip(character, INTIGER))
        res = 0
        for i in RS:
            res += dict_guid.get(i)
        return res
