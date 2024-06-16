#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for row in matrix:
        res_row = []
        for i in range(len(matrix)):
            res_row.append(row[i] * row[i])
        res.append(res_row)
    return res
