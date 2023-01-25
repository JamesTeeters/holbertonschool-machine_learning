#!/usr/bin/env python3
"""Poisson distribution class"""


class Poisson:
    """Class for Poisson"""
    def __init__(self, data=None, lambtha=1.):
        """docstring for Poisson"""
        self.data = data
        """Data = list of data points"""
        self.lambtha = float(lambtha)
        """lambtha = mean number of data points, must be float"""
        if data is not None:
            """check to see if data exists"""
            if type(data) is not list:
                """data is not a list"""
                raise TypeError("data must be a list")
            elif len(data) < 2:
                """data is less than 2"""
                raise ValueError("data must contain multiple values")
            else:
                """calculate lambtha from data"""
                self.lambtha = float(sum(data) / len(data))
        else:
            """data is None"""
            if lambtha <= 0:
                """lambtha must be greater than 0"""
                raise ValueError("lambtha must be a positive value")
            else:
                """use lambtha as mean number of data points"""
                data = lambtha

    def pmf(self, k):
        """Calculates thes value of the PMF for a given number of successes
            k = number of successes
        """
        """mathmatical constant"""
        e = 2.7182818285
        k = int(k)
        if k < 0:
            return float(0)

        """factorial of k"""
        fact = 1
        for i in range(1, k + 1):
            fact = int(i * fact)
        """PMF function for poisson distribution"""
        return ((e ** -self.lambtha) * (self.lambtha ** k)) / fact
