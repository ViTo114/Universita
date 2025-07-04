import numpy as np


class LinearRegression:

    def __init__(self, learningRate=1, lmd=1, numeroIterate=200, numeroFeature=5):
        self.learningRate = learningRate
        self.lmd = lmd
        self.numeroIterate = numeroIterate
        self.numeroFeature = numeroFeature

        self.lmd_ = np.full(numeroFeature, lmd)
        lmd_[0] = 0