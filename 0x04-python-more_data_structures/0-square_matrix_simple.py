#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    else:
        row = range(len(matrix))
        col = range(len(matrix[0]))
        new_matrix = [[0 for _ in col]for _ in row]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
