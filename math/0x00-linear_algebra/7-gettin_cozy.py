#!/usr/bin/env python3
"""concatenate two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenate two matrices along a specific axis"""
    new_mat = []
    if axis == 0:
        for i in range(len(mat1)):
            new_mat.append(mat1[i].copy())
        for i in range(len(mat2)):
            new_mat.append(mat2[i].copy())
        return new_mat
    if axis == 1:
        for j in range(len(mat1)):
            new_mat.append(mat1[j].copy() + mat2[j].copy())
        return new_mat
