#!/usr/bin/python3
def max_integer(my_list=[]):
    Comp_num = my_list[0]
    if len(my_list) < 1:
        return None
    else:
        for i in my_list:
            if i > Comp_num:
                Comp_num = i
            else:
                continue
        return Comp_num
