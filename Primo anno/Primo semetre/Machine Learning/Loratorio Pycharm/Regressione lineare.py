from xml.etree.ElementPath import prepare_descendant

import numpy as np

class RegressioneLineare:
    def __init__(self, numeroIterate, numeroVariabili, seed, learningRate):
        self.numeroItearte = numeroIterate
        self.numeroVariabili = numeroVariabili
        self.learningRate = learningRate

        self.seed = seed
        np.random.seed(seed)

        self.theta = np.random.rand(self.numeroFeature)


    def fit_bgd(self, X, Y):
        m = X.shape[0]

        thetaHistory = np.zerso((self.numeroItearte, self.numeroVariabili))
        costFunctionHistory = np.zerso(self.numeroItearte)

        for epoca in range(0, self.numeroItearte):
            predizioni = np.dot(X, self.theta)

            errori = predizioni - Y

            self.theta = self.theta - self.learningRate * (1/m) * np.dot(X.T, errori)

            thetaHistory[epoca] = self.theta
            costFunctionHistory[epoca] = (1/(2*m)) * np.dot(errori.T, errori)


    def fit_mbgd(self, X, Y, batchSize):
        m = X.shape[0]

        thetaHistory = np.zeros((self.numeroItearte, self.numeroVariabili))
        costFunctionHistory = np.zeros(self.numeroIterate)

        for epoca in range(0, self.numeroItearte):
            for indice in range(0,m, batchSize):
                xRidotto = X[indice:indice+batchSize, :]
                yRidotto = Y[indice:indice+batchSize]

                predizioni = np.dot(xRidotto, self.theta)
                errori = predizioni - yRidotto

                self.theta = self.theta - self.learningRate * (1/batchSize) * np.dot(X.T, errori)


                predizioniComplete = np.dot(X, self.theta)
                erroriCompleti = predizioniComplete - Y

                thetaHistory[epoca] = self.theta
                costFunctionHistory[epoca] = (1/(2*m)) * np.dot(erroriCompleti.T, erroriCompleti)



    def fit_sgd(self,X,Y):
        m = X.shape[0]

        thetaHistory = np.zeros((self.numeroItearte, self.numeroVariabili))
        costFunctionHistory = np.zeros(self.numeroItearte)

        for i in range(0, self.numeroItearte):
            indice = np.random.randint(m)

            x = X[indice]
            y = Y[indice]

            predizione = np.dot(x, self.theta)
            errore = predizione - y

            self.theta = self.theta - self.learningRate * np.dot(x.T, errore)

            predizioniComplete = np.dot(X, self.theta)
            erroriCompleti = predizioniComplete - Y

            thetaHistory[epoca] = self.theta
            costFunctionHistory[epoca] = (1/(2*m)) * np.dot(erroriCompleti.T, erroriCompleti)

