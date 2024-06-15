#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, elem in enumerate(row):
            if i > 0:
                print("{}".format(" "), end="")
            print("{:d}".format(elem), end="")
        print()
