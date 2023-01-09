#!/usr/bin/env python3
"""get the shape of a matrix"""
def matrix_shape(matrix):
    try:
        return([len(matrix)] + matrix_shape(matrix[0]))
    except Exception:
        return([])
