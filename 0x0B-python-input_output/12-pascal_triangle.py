#!/usr/bin/python3
"""
Defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    n = 5
    result = pascal_triangle(n)

    for row in result:
        print("[{}]".format(",".join([str(x) for x in row])))
