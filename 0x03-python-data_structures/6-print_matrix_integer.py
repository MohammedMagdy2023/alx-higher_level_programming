#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) <= 0:
        return None
    else:
        for i in matrix:
            for j in i:
                print(" ".join("{:d}".format(j)))
            print()
