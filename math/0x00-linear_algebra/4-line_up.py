#!/usr/bin/env python3
"""adds two arrays element-wise:"""


def add_arrays(arr1, arr2):
    """adds two arrays"""
    new_arr = []
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            new_arr.append(arr1[i] + arr2[i])
        return new_arr
