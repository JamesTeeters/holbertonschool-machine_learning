#!/usr/bin/env python3
"""converts a numeric label vector into a one-hot matrix"""
import numpy as np


def one_hot_encode(Y, classes):
    """encode a numeric label vector into a one-hot matrix"""
    if Y is None or classes is None:
        return None
    try:
        """m = number of examples"""
        m = Y.shape[0]
        one_hot = np.zeros(shape=(classes, m))

        for i in range(m):
            one_hot[Y[i]][i] = 1

        return one_hot
    except Exception:
        return None
