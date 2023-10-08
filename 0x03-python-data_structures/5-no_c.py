#!/usr/bin/python3
def no_c(my_string):
    new_list = ''
    for i in range(0,len(my_string)):
        if my_string[i] == "c" or "C":
            continue
        else:
            new_list += my_string[i]
    return new_list
