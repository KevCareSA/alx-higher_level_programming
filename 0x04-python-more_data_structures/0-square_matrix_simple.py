#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_sqr_mtrx = []
    for row in matrix:
        newRow = sq_list(row)
        new_sqr_mtrx.append(newRow)
    return new_sqr_mtrx


def sq_list(x):
    return [i**2 for i in x]
