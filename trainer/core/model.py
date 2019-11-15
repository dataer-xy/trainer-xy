

import tensorflow as tf
import numpy as np
from .modelconfig import modelConfig

class LineModel(object):
    def __init__(self):

        self.x = tf.placeholder(dtype=tf.float64,shape=[None,2],name="x")
        self.yTrue = tf.placeholder(dtype=tf.float64,shape=[None],name="yTrue")
        # 构造一个线性模型
        b = tf.Variable(tf.zeros([1]),name="bias")
        W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0),name="weight")
        yHat = tf.matmul(W, self.x) + b

        # 最小化方差
        self.loss_op = tf.reduce_mean(tf.square(yHat - self.yTrue))
        self.accuracy_op = 1-tf.reduce_sum(tf.square(yHat - self.yTrue)) / self.deno # 区别于R2，固定值
        optimizer = tf.train.GradientDescentOptimizer(modelConfig.learningRate)
        self.train_op = optimizer.minimize(self.loss_op)




