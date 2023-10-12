#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) or roman_string == None:
        return 0
    else:
        character = ["I", "V", "X", "L", "C", "D", "M"]
        INTIGER = [1, 5, 10, 50, 100, 500, 1000]
        dict_guid = dict(zip(character, INTIGER))
        res = 0
        for i in range(len(roman_string)):
            if (i > 0 and 
                dict_guid[roman_string[i]] > dict_guid[roman_string[i - 1]]):
                res += (dict_guid[roman_string[i]] - 
                        2 * dict_guid[roman_string[i - 1]])
            else:
                res += dict_guid[roman_string[i]]
        return res
