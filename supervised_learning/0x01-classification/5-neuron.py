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

    def evaluate(self, X, Y):
        """function to evaluate predictions"""
        A = self.forward_prop(X)
        C = self.cost(Y, A)
        vector = np.vectorize(np.int_)
        return (vector(A.round()), C)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """gradient descent"""
        """m = num of examples"""
        m = Y.shape[1]
        """dz = derivative of cost function"""
        dz = A - Y
        """dw = derivative of weight"""
        dw = (1/m)*(np.matmul(dz, X.T))
        """db = derivative of bias"""
        db = (1/m)*(np.sum(A-Y))

        self.__W = self.__W - (alpha * dw)
        self.__b = self.__b - (alpha * db)
