#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or type(roman_string) == None:
        return 0
    else:
        character = ["I", "V", "X", "L", "C", "D", "M"]
        INTIGER = [1, 5, 10, 50, 100, 500, 1000]
        dict_guid = dict(zip(character, INTIGER))
        res = 0
        for i in roman_string:
            res += dict_guid.get(i)
        return res
