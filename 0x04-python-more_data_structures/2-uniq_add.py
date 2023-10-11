#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return my_list
    else:
        res = 0
        checked = []
        for i in my_list:
            if i in checked:
                continue
            else:
                res += i
                checked.append(i)
    return res
