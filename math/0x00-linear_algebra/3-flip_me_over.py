#!/usr/bin/env python3
"""return the transpose of a 2D matrix,"""


def matrix_transpose(matrix):
    """use zip to transpose and map to make output lists """
    return list(map(list, zip(*matrix)))
