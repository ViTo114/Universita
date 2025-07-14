import numpy as np

seed = 42
np.random.seed(seed)

def sigmoid(n):
    return 1 / (1 + np.exp(-n))

class NeuralNetwork:
    def __init__(self, learningRate, numeroIterate, lmd, layers):
        self.learningRate = learningRate
        self.numeroIterate = numeroIterate
        self.lmd = lmd

        self.layers = layers
        self.numeroLayers = len(layers)

        self.pesi = {}
        self.bias = {}


    def inizializzazionePesi(self):
        for i in range(1, self.numeroLayer):
            self.pesi[i] = np.random.rand((self.layers[i], self.layers[i-1]))
            self.bias[i] = np.ones(self.layers[i])


    def forwardPropagation(self, X):
        values = {}

        for i in range(1, self.numeroLayers):
            if i == 1:
                values["Z" + str(i)] = np.dot(self.pesi[i], X.T) + self.bias[i]
                values["A" + str(i)] = sigmoid(values["Z" + str(i)])

            else:
                values["Z" + str(i)] = np.dot(self.pesi[i], values["A", str(i-1)])
                values["A" + str(i)] = sigmoid(values["Z" + str(i)])


    







