#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for e in matrix:
        n_row = []
        for j in e:
            n_row.append(j*j)
        n_matrix.append(n_row)
    return n_matrix
