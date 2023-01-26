#!/usr/bin/env python3
"""Exponential Distibution"""


class Exponential:
    """class for exponential distribution"""
    def __init__(self, data=None, lambtha=1.):
        """define parameters for exponential distribution"""

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

    def pdf(self, x):
        """Calculates thes value of the PDF for a given number of successes"""

        e = 2.7182818285
        """ e = mathmatical constant"""
        """x is time period, must be positive"""
        if x < 0:
            return 0

        """PDF function for poisson distribution"""
        return self.lambtha * (e ** (-self.lambtha * x))

    def cdf(self, x):
        """Calculates thes value of the cdf for a given number of successes"""
        e = 2.7182818285
        """e = mathmatical constant"""
        """x is the time period, must be positive"""
        if x <= 0:
            return 0

        """cdf function for poisson distribution"""
        sum = 0
        """sum of pmf calculations of given success"""
        for i in range(0, x + 1):
            sum += self.pdf(i)
        return sum