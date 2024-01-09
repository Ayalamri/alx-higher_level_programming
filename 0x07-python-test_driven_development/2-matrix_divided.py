#!/usr/bin/python3
'''Module for matrix division.'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix by a number.'''
    if not matrix or not all(matrix) or not all(map(lambda row: len(row) == len(matrix[0]), matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
