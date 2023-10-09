#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) <= 0:
        return None
    else:
        for row in matrix:
            print(" ".join("{:d}".format(elem) for elem in row))
