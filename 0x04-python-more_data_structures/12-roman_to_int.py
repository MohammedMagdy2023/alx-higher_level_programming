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
        for i in range(len(RS)):
            if (i > 0 and dict_guid[RS[i]] > dict_guid[RS[i - 1]]):
                res += (dict_guid[RS[i]] - 2 * dict_guid[RS[i - 1]])
            else:
                res += dict_guid[RS[i]]
        return res
