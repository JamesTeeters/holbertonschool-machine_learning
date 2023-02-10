#!/usr/bin/env python3
"""create placeholder in tesorflow"""
import tensorflow as tf


def create_placeholders(nx, classes):
    """create placeholders"""
    x = tf.placeholder(tf.float32, [None, nx], name="x")
    y = tf.placeholder(tf.float32, [None, classes], name="y")

    return x, y
