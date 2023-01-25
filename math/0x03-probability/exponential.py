#!/usr/bin/env python3
"""Exponential Distibution"""


class Exponential:
    def __init__(self, data=None, lambtha=1.):
        """class for exponential distribution"""

        self.data = data
        """Data = list of data points"""
        self.lambtha = float(lambtha)
        """lambtha = excpected number of occurances, must be float"""
        if data is not None:
            """check to see if data exists"""
            if type(data) is not list:
                """check to see if data is a list"""
                raise TypeError("data must be a list")
            elif len(data) < 2:
                """check to see if data is correct length"""
                raise ValueError("data must contain multiple values")
            else:
                """calculate lambtha from data"""
                self.lambtha = float(1 / (sum(data) / len(data)))
        else:
            """data is None"""
            if lambtha <= 0:
                """lambtha must be positive"""
                raise ValueError("lambtha must be a positive value")
            else:
                """use given lambtha as data value"""
                data = lambtha
