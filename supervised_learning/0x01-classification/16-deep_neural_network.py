#!/usr/bin/env python3
"""deep neural network"""
import numpy as np


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

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for i in range(1, self.L):
            if type(layers[i]) is not int or layers[i] < 1:
                raise TypeError("layers must be a list of positive integers")
            if i > 0:
                self.weights["W" + str(i)] = np.random.randn(
                    layers[i], layers[i-1])*np.sqrt(2/layers[i-1])
                self.weights["b" + str(i)] = np.zeros(shape=(layers[i], 1))
            if i == 0:
                self.weights["W1"] = np.random.randn(
                    layers[i], nx)*np.sqrt(2/nx)
                self.weights["b1"] = np.zeros(shape=(layers[i], 1))
