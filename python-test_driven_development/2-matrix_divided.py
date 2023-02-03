#!/usr/bin/python3
"""
This is the "matrix_divided" module.

The module supplies one function, matrix_divided(). Eg,

>>>matrix_divided(12, 3)
4
"""


def matrix_divided(matrix, div):
    """
    Returns new_matrix
    """
    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same" +
                            " size")
        for s in row:
            if type(s) not in [int, float]:
                raise TypeError("matrix must " +
                                "be a matrix (list of lists) of integers/floats")
            result = s/div
            new_row.append(round(result, 2))

        new_matrix.append(new_row)
    return new_matrix
