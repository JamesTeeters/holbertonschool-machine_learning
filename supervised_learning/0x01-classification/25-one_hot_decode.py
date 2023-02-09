#!/usr/bin/env python3
"""converts a one-hot matrix into a vector of labels"""
import numpy as np


def one_hot_decode(one_hot):
    """decode a one-hot matrix into a vector of labels"""
    try:
        """classes = max number of classes"""
        """m = number of examples"""
        classes, m = one_hot.shape

        vector = np.zeros(shape=(m,))
        for i in range(m):
            for j in range(classes):
                if one_hot[j][i] == 1:
                    vector[i] = j
        return int(vector)
    except Exception:
        return None
