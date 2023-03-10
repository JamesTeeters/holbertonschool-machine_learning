#!/usr/bin/env python3
"""concatenate two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenate two matrices along a specific axis"""
    new_mat = []
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        else:
            for i in range(len(mat1)):
                new_mat.append(mat1[i].copy())
            for i in range(len(mat2)):
                new_mat.append(mat2[i].copy())
            return new_mat
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        else:
            for j in range(len(mat1)):
                new_mat.append(mat1[j].copy() + mat2[j].copy())
            return new_mat
