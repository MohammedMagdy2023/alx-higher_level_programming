#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        n1 = n2 = 0
        for i, j in my_list:
            n1 += i * j
            n2 += j
        avg = n1 / n2
        return avg