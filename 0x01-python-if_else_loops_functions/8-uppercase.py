#!/usr/bin/python3
def uppercase(str):
    R_string = ""
    for i in str:
        if ord(i) in range(97, 123):
            R_string += chr(ord(i) - 32)
        else:
            R_string += i
    print("{}".format(R_string))
