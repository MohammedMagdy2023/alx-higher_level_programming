#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) <= 0:
        return None
    else:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                print(matrix[i][j], end= "")
            print()
