#!/usr/bin/env python3
"""Binomial Distibution"""
pi = 3.1415926536
"""pi is mathmatical constant"""
e = 2.7182818285
"""e is mathmatical constant"""


class Binomial:
    """class for Binomial distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        """initialize the Binomial distribution"""
        self.data = data
        """data is a list of data points"""
        self.n = int(n)
        """n is the number of trials in the distribution"""
        self.p = float(p)
        """p is the probability of success"""

        if data is None:
            if n < 0:
                raise ValueError('n must be a positive value')
            elif p < 0 or p > 1:
                raise ValueError('p must be greater than 0 and less than 1')
        else:
            if type(data) != list:
                raise ValueError('data must be a list')
            elif len(data) < 2:
                raise ValueError('data must contain multiple values')
            else:
                mean = sum(data) / len(data)
                """mean is mean of all values"""
                data_sum = 0
                """data_sum is the sum of data points minus the mean squared"""
                for i in data:
                    data_sum += (i - mean) ** 2
                """stddev is the square root of the mean of data_sum"""
                stddev = (data_sum / len(data)) ** (1/2)
                self.p = 1-(mean/stddev)
                self.n = round(sum(data)/self.p)/len(data)
                self.p = mean/stddev
