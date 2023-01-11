#!/usr/bin/env python3
"""that adds two matrices element-wise:"""


def add_matrices2D(mat1, mat2):
    """add two matrices element-wise"""
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    else:
        new_arr = []
        new_matrix = []
        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                new_arr.append(mat1[i][j] + mat2[i][j])
            new_matrix.append(new_arr)
            new_arr = []
        return new_matrix


def matrix_shape(matrix):
    """use recursion to get the length of all arrays"""
    try:
        return([len(matrix)] + matrix_shape(matrix[0]))
    except Exception:
        return([])
