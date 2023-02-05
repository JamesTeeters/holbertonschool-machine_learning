#!/usr/bin/env python3
"""Class for neuron"""
import numpy as np


def sig(x):
    """sigmoid activation function"""
    return (1 / (1 + np.exp(-x)))


class Neuron:
    """Class for neuron"""
    def __init__(self, nx):
        """initialize the neuron"""
        self.__b = 0
        """private bias variable"""
        self.__A = 0
        """private activated output variable"""
        self.__W = np.random.randn(1, nx)
        """private weight variable"""

        if type(nx) is not int:
            """check to see if nx is an integer"""
            raise TypeError('nx must be an interger')
        if nx < 1:
            """check to see if nx is positive"""
            raise ValueError('nx must be a positive integer')

    @property
    def A(self):
        """output property getter"""
        return self.__A

    @property
    def b(self):
        """bais property getter"""
        return self.__b

    @property
    def W(self):
        """weight property getter"""
        return self.__W

    def forward_prop(self, X):
        """calculate forward propagation"""
        self.X = X
        a1 = np.matmul(self.W, X) + self.b
        """weighted sum of inputs"""
        """
        X is numpy array; shape(nx, m); contains input data
        nx is the number of input factors
        m is the number of examples
        """
        self.__A = sig(a1)
        return self.__A

    def cost(self, Y, A):
        """Cost function"""
        return np.sum(-(Y*np.log(A)+(1-Y)*np.log(1.0000001 - A)))/Y.shape[1]
