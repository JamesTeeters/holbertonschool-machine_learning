#!/usr/bin/env python3
"""normal distribution"""


class Normal:
    """Class for normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """initialize the normal distribution"""
        self.data = data
        """data is a list of data points"""
        self.mean = float(mean)
        """mean is the mean of the distribution"""
        self.stddev = float(stddev)
        """stddev is the standard deviation of the distribution"""

        if data is None:
            """check to see if data exists"""
            if stddev <= 0:
                """check to see if stddev is positive"""
                raise ValueError('stddev must be a positive value')
        else:
            if type(data) != list:
                """check to see if data is a list"""
                raise TypeError("data must be a list")
            elif len(data) < 2:
                """check to see if data has multiple elements"""
                raise ValueError("data must contain multiple values")
            else:
                self.mean = sum(data) / len(data)
                """set mean to correct value"""
                data_sum = 0
                """data_sum is the sum of data points minus the mean squared"""
                for i in data:
                    data_sum += (i - self.mean) ** 2
                """stddev is the square root of the mean of data_sum"""
                self.stddev = (data_sum / len(data)) ** (1/2)
