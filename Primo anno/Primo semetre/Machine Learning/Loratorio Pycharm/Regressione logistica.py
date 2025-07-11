import numpy as np

class RegressioneLogistica:
    def __init__(self, numeroIterate, numeroFeature, seed, learningRate):
        self.numeroIterate = numeroIterate
        self.numeroFeature = numeroFeature
        self.learningRate = learningRate

        np.random.seed(seed)
        self.theta = np.random.rand(numeroFeature)


    @staticmethod
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))


    def fit_fullBatch(self, X, y):
        m = X.shape[0]

        thetaHistory = np.zeros((self.numeroIterate, self.theta.shape[0]))
        costFunctionHistory = np.zeros(self.numeroIterate)

        for epoca in range(0, self.numeroIterate):
            z = np.dot(X, self.theta)
            predizoni = self.sigmoid(z)

            errori = predizoni - y

            self.theta = self.theta - self.learningRate / m * np.dot(X.T, errori)

            thetaHistory[epoca] = self.theta
            costFunctionHistory[epoca] - (1/m) * (np.dot(y, np.log(predizoni)) + np.dot((1 -y), np.log(1-predizoni)))