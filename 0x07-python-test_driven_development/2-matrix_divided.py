#!/usr/bin/python3

"""This module holds the function matrix_divided which takes a matrix
and divides each element by 3
"""


def matrix_divided(matrix, div):

    """Divides the matrix"""
    err = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if type(matrix) != list or any(type(n) != list for n in matrix):
        raise TypeError(err)

    if not matrix or any(not row for row in matrix):
        raise TypeError(err)

    if any(any(type(i) != int and type(i) != float for i in r)for r in matrix):
        raise TypeError(err)

    if any(not row for row in matrix):
        raise TypeError(err)

    lenght = len(matrix[0])
    if any(len(row) != lenght for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    return [[round(col / div, 2) for col in row] for row in matrix]
