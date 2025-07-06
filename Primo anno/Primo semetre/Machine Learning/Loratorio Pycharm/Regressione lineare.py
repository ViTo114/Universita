import numpy as np


class LinearRegression:

    def __init__(self, learningRate, numeroIterate, numeroFeature, seed):
        self.learningRate = learningRate
        self.numeroIterate = numeroIterate
        self.numeroFeature = numeroFeature
        self.seed = seed

        np.random.rand(self.seed)

        self.theta = np.random(self.numeroFeature)


    def fit_fullBatch(self, X, Y):
        m = X.shape[0]

        thetaHistory = np.zeros(self.numeroIterate, self.theta.shape[0])
        costFunctionHistory = np.zeros(self.numeroIterate)

        for epoca in range(0, self.numeroIterate):

            predizioni = np.dot(X, self.theta)

            errori = Y - predizioni

            gradiente = np.dot(X.T, errori)

            self.theta = self.theta - self.learningRate * (1/m) * gradiente

            thetaHistory[epoca] = self.theta
            costFunctionHistory[epoca] = (1/(2*m)) * np.dot(errori.T, errori)


    def fit_miniBatch(self, X, Y, batchSize):
        m = X.shape[0]

        thetaHistory = np.zeros(self.numeroIterate, self.theta.shape[0])
        costFunctionHistory = np.zeros(self.numeroIterate)

        for epoca in range(0, self.numeroIterate):
            for indice in range(0, m, batchSize):

                xRidotto = X[indice:indice+batchSize, :]
                yRidotto = Y[indice:indice+batchSize]

                predizioni = np.dot(X, self.theta)

                errori = yRidotto - predizioni

                gradiente = np.dot(xRidotto.T, errori)

                self.theta = self.theta - self.learningRate * (1/m) * gradiente


            thetaHistory[epoca] = self.theta
            costFunctionHistory[epoca] = (1/(2*m)) * np.dot(errori.T, errori.T)



    def fit_sgd(self, X, Y):
        m = X.shape[0]

        thetaHistory = np.zerso(self.numeroIterate, self.theta.shape[0])
        costFunctionHistory = np.zeros(self.numeroIterate)

        for epoca in range(0, self.numeroIterate):

            indice = np.random.rand(m)

            x = X[indice]
            y = Y[indice]

            predizione = np.dot(x, self.theta)

            errore = y - predizione

            gradiente = np.dot(X.T, errore)

            self.theta = self.theta - self.learningRate * gradiente

            thetaHistory[epoca] = self.theta
            costFunctionHistory = (1/2) * np.dot(errore.T, errore)



    def fit_normalEquation(self, X, Y):

        self.theta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), Y)