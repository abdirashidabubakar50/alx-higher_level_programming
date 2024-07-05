#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and rounds the result to 2 decimal places.

    Args:
        matrix (list of list of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of list of float: A new matrix with all elements divided by the divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats, if each row of the matrix is not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix is of the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if the div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]
