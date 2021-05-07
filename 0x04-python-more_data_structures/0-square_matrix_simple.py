#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        new.append([n ** 2 for n in row])
    return new
