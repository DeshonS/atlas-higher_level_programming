#!/usr/bin/python3
"""creates a pascal triangle based on n"""


def pascal_triangle(n):
    """init pascal_triangle"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
