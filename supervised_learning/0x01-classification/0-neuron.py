#!/usr/bin/env python3
"""create a class for a neuron"""
import numpy as np


class Neuron:
    """class for a neuron"""
    def __init__(self, nx):
        """initialize a neuron"""
        self.nx = nx
        """nx = the number of input features to the neuron"""

        if type(self.nx) is not int:
            """check if a neuron is an integer"""
            raise TypeError('nx must be an integer')
        if nx < 1:
            """check if a neuron is positive"""
            raise ValueError('nx must be a positive integer')

        self.W = np.random.randn(1, nx)
        """w = weicght vector for neuron"""
        self.b = 0
        """b = bias"""
        self.A = 0
        """A = activated output of neuron"""
