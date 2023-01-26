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

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        self.x = x
        """x is the x-value"""
        return (self.x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        self.z = z
        """z is the z-score"""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value"""
        self.x = x
        """x is the x-value"""
        pi = 3.1415926536
        """pi is mathmatical constant"""
        e = 2.7182818285
        """e is mathmatical constant"""
        """return is pdf formula for normal distribution"""
        return ((1 / (self.stddev * ((2 * pi) ** .5))) *
                (e ** (-.5 * ((x - self.mean) / self.stddev) ** 2)))
