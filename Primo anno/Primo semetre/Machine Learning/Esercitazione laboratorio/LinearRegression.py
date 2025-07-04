import numpy as np


class LinearRegression:

    def __init__(self, learningRate=1, lmd=1, numeroIterate=200, numeroFeature=5):
        self.learningRate = learningRate
        self.lmd = lmd
        self.numeroIterate = numeroIterate
        self.numeroFeature = numeroFeature

        #Questa istruzione mi creare un vettore numpy di numeroFeature elementi tutti con il valore lmd
        self.lmd_ = np.full(numeroFeature, lmd)
        self.lmd_[0]=0



        