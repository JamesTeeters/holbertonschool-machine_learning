#!/usr/bin/env python3
"""neural network"""
import numpy as np


def sig(x):
    """sigmoid activation function"""
    return (1 / (1 + np.exp(-x)))


class NeuralNetwork:
    """class for Neural Network"""
    def __init__(self, nx, nodes):
        """initialize a Neural Network"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise ValueError("nx must be a positive integer")
        elif type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        elif nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros(shape=(nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """getter for the W1"""
        return self.__W1

    @property
    def b1(self):
        """getter for the b1"""
        return self.__b1

    @property
    def A1(self):
        """getter for the A1"""
        return self.__A1

    @property
    def W2(self):
        """getter for the W2"""
        return self.__W2

    @property
    def b2(self):
        """getter for the b2"""
        return self.__b2

    @property
    def A2(self):
        """getter for the A2"""
        return self.__A2

    def forward_prop(self, X):
        """forward propagate the neural network"""

        z1 = np.matmul(self.__W1, X) + self.__b1
        """product from imput to hidden layer"""
        self.__A1 = sig(z1)
        """activation function to hidden layer"""
        z2 = np.matmul(self.__W2, self.__A1) + self.__b2
        """product from hidden layer to output layer"""
        self.__A2 = sig(z2)
        """activation function to output layer"""

        return self.__A1, self.__A2

    def cost(self, Y, A):
        """cost function for neural network"""
        return np.sum(-(Y*np.log(A)+(1-Y)*np.log(1.0000001 - A)))/Y.shape[1]
    
    def evaluate(self, X, Y):
        """Evaluates the neural network's predictions"""
        A1, A2 = self.forward_prop(X)
        C = self.cost(Y, A2)
        vector = np.vectorize(np.int_)
        return (vector(A2.round()), C)
