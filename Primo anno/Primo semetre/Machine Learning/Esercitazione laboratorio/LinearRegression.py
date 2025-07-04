from contextlib import nullcontext

import numpy as np


class LinearRegression:

    def __init__(self, learningRate=1, lmd=1, numeroIterate=200, numeroFeature=5, seed=123):
        self.learningRate = learningRate
        self.lmd = lmd
        self.numeroIterate = numeroIterate
        self.numeroFeature = numeroFeature

        #Queste istruzione mi imposta il seed per tutte le operazione casuali
        self.seed = seed
        np.random.seed(self.seed)

        #Questa istruzione mi definice il vettore dei pesi. In particolare mi restituisce un vettore di pesi casuali
        self.theta=np.random.rand(numeroFeature)

        #Queste istruzione mi creare un vettore numpy di numeroFeature elementi tutti con il valore lmd
        self.lmd_ = np.full(numeroFeature, lmd)
        self.lmd_[0]=0




    def fbgd_fit(self, X_training, Y_training):
        theta_history = np(self.numeroFeature)


