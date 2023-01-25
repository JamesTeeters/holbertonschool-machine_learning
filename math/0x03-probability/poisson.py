#!/usr/bin/env python3
"""Poisson distribution class"""


class Poisson:
    """Class for Poisson"""
    def __init__(self, data=None, lambtha=1.):
        """poisson distribution class"""

        self.data = data
        """Data = list of data points"""
        self.lambtha = float(lambtha)
        """lambtha = mean number of data points, must be float"""
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
                self.lambtha = float(sum(data) / len(data))
        else:
            """data is None"""
            if lambtha <= 0:
                """lambtha must be positive"""
                raise ValueError("lambtha must be a positive value")
            else:
                """use given lambtha as data value"""
                data = lambtha

    def pmf(self, k):
        """Calculates thes value of the PMF for a given number of successes"""

        e = 2.7182818285
        """ e = mathmatical constant"""
        k = int(k)
        """k is number of success, must be positive integer"""
        if k < 0:
            return 0

        """PMF function for poisson distribution"""
        return ((e ** -self.lambtha) * (self.lambtha ** k)) / self.factorial(k)

    def cdf(self, k):
        """Calculates thes value of the cdf for a given number of successes"""
        x = 0
        e = 2.7182818285
        """e = mathmatical constant"""
        k = int(k)
        """k is number of success, must be positive integer"""
        if k < 0:
            return 0

        """cdf function for poisson distribution"""
        sum = 0
        """sum of pmf calculations of given success"""
        for i in range(0, k + 1):
            sum += self.pmf(i)
        return sum

    def factorial(self, n):
        """factorial function"""
        fact = 1
        for i in range(1, n + 1):
            fact = int(i * fact)
        return fact
