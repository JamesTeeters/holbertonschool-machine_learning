#!/usr/bin/env python3
"""deep neural network"""
import numpy as np


def sig(x):
    """sigmoid activation function"""
    return (1 / (1 + np.exp(-x)))


class DeepNeuralNetwork:
    """class for DeepNeuralNetwork"""
    def __init__(self, nx, layers):
        """initialize DeepNeuralNetwork"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for i in range(self.__L):
            if type(layers[i]) is not int or layers[i] <= 0:
                raise TypeError("layers must be a list of positive integers")
            if i > 0:
                self.__weights["W" + str(i + 1)] = np.random.randn(
                    layers[i], layers[i-1])*np.sqrt(2/layers[i-1])
                self.__weights["b" + str(i + 1)] =\
                    np.zeros(shape=(layers[i], 1))
            if i == 0:
                self.__weights["W1"] = np.random.randn(
                    layers[i], nx)*np.sqrt(2/nx)
                self.__weights["b1"] = np.zeros(shape=(layers[i], 1))

    @property
    def weights(self):
        """getter for the weights"""
        return self.__weights

    @property
    def cache(self):
        """getter for the cache"""
        return self.__cache

    @property
    def L(self):
        """getter for L"""
        return self.__L

    def forward_prop(self, X):
        """forward propagate the deep neural network"""
        for i in range(self.__L + 1):
            if i == 0:
                """store X in cache"""
                self.__cache["A0"] = X
            else:
                """z is input modified with weights and bias"""
                z = np.matmul(self.__weights["W" + str(i)],
                              self.__cache["A" + str(i-1)])\
                    + self.__weights["b" + str(i)]
                """store activated output in the cache"""
                self.__cache["A" + str(i)] = sig(z)

        return self.__cache["A" + str(self.__L)], self.__cache

    def cost(self, Y, A):
        """Cost function"""
        return np.sum(-(Y*np.log(A)+(1-Y)*np.log(1.0000001 - A)))/Y.shape[1]
