#!/usr/bin/env python3
"""get the shape of a matrix"""


def matrix_shape(matrix):
    """use recursion to get the length of all arrays"""
    try:
        return([len(matrix)] + matrix_shape(matrix[0]))
    except Exception:
        return([])
