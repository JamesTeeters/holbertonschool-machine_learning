#!/usr/bin/env python3
"""Poisson distribution class"""


class Poisson:
    """Class for Poisson"""
    def __init__(self, data=None, lambtha=1.):
        """docstring for Poisson"""
        self.data = data
        """Data = list of data points"""
        self.lambtha = float(sum(data) / len(data)) if data else lambtha
        """lambtha = mean number of data points"""

        if data is not None:
            """check to see if data exists"""
            if type(data) != list:
                """data is not a list"""
                raise TypeError("data must be a list")
            elif len(data) < 2:
                """data is less than 2"""
                raise ValueError("data must contain multiple values")
        else:
            """data is None"""
            if lambtha <= 0:
                """lambtha must be greater than 0"""
                raise ValueError("lambtha must be a positive value")
            else:
                """use lambtha as mean number of data points"""
                data = lambtha
