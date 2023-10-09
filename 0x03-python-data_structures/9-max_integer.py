#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        Comp_num = my_list[0]
        for i in my_list:
            if i > Comp_num:
                Comp_num = i
            else:
                continue
        return Comp_num
