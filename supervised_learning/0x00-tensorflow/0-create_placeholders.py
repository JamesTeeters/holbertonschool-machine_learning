#!/usr/bin/env python3

import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()

def create_placeholders(nx, classes):

    x = tf.placeholder(tf.float32, [None, nx], name="x")
    y = tf.placeholder(tf.float32, [None, classes], name="y")

    return x, y
