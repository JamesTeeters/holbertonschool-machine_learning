#!/usr/bin/env python3
"""create placeholder in tesorflow"""
import tensorflow as tf
create_layer = __import__('1-create_layer').create_layer
"""import create_layer from 1-create_layer.py"""


def create_placeholders(nx, classes):
    """create placeholders"""
    x = tf.placeholder(tf.float32, [None, nx], name="x")
    y = tf.placeholder(tf.float32, [None, classes], name="y")

    return x, y
