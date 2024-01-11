#!/usr/bin/python3
"""
Prints a square with the character #
"""


def print_square(size):
    """Prints a square with the character #
    
    Args:
    - size (int): The size length of the square
    
    Raises:
    - TypeError: If size is not an integer or if it's a float
    - ValueError: If size is less than 0
    
    Returns:
    - None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
