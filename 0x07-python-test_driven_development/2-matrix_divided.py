#!/usr/bin/python3
"""
Divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.

    Args:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Raises:
    - TypeError: If matrix is not a list of lists of integers/floats,
                 or if div is not a number (integer or float).
    - ZeroDivisionError: If div is equal to 0.
    - TypeError: If each row of the matrix doesn't have the same size.

    Returns:
    - A new matrix with elements rounded to 2 decimal places.
    """

    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
