def square_matrix_simple(matrix=[]):
    res = []
    for row in matrix:
        res_row = []
        length = len(row)
        for i in range(length):
            res_row.append((row[i] * row[i]))
        res.append(res_row)
    return res
