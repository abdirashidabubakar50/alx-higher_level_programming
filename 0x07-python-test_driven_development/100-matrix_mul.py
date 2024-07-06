#!/usr/bin/python3
"""This module defines a function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        A new matrix that is the product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, or if the elements of the lists
                   are not lists of integers or floats.
        ValueError: If m_a or m_b is empty, or if the matrices cannot be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lits")
    if not m_a or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not m_b or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should only contain intgers or floats")
    size_m_a = len(m_a[0])
    for row in m_a:
        if (len(row) != size_m_a):
            raise TypeError("each row of m_a must be of the same size")
    
    size_m_b = len(m_b[0])
    for row in m_b:
        if (len(row) != size_m_b):
            raise TypeError("each row of m_b must be of the same size")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            sum_product = 0
            for k in range(len(m_a[0])):
                sum_product += m_a[i][k] * m_b[k][j]
            result_row.append(sum_product)
        result.append(result_row)

    return result
