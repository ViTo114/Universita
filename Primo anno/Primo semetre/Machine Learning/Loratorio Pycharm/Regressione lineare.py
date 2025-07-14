import numpy as np

class RegressioneLineare:
    def __init__(self, numeroIterate, numeroFeature, learningRate, seed, lmd):
        self.numeroIterate = numeroIterate
        self.numeroFeature = numeroFeature
        self.learningRate = learningRate

        self.seed = seed
        np.random.seed = seed

        self.theta = np.random.rand(numeroFeature)


        self.lmd = np.zeros(numeroFeature)
        self.lmd = np.full(numeroFeature, lmd)
        self.lmd[0] = 0


    def fit_fbg(self, X, y):
        m = X.shape[0]

        thetaHistory = np.zeros((self.numeroIterate, self.numeroFeature))
        costHistoryFunction = np.zeros(self.numeroIterate)

        for epoca in range(0, self.numeroIterate):
            predizioni = np.dot(X, self.theta)

            errori = predizioni - y

            self.theta = self.theta - self.learningRate / m * (np.dot(X.T,errori) + self.lmd * self.theta)

        thetaHistory[epoca] = self.theta
        costHistoryFunction[epoca] = (1/(2*m)) * (np.to(errori.T, errori) + self.lmd * np.dot(self.theta[1:].T, self.theta[1:]))


    def fit_bgd(self, X, y, batchSize):
        m = X.shape[0]

        thetaHistory = np.zeros((self.numeroIterate, self.numeroFeature))
        costFunctionHistory = np.zeros(self.numeroIterate)

        for epoca in range(0, self.numeroIterae):
            for indice in range(0, m , batchSize):
                xRiodotto = X[indice:indice+batchSize, :]
                yRidotto = y[indice:indice+batchSize]

                predizioni = np.dot(xRiodotto, self.theta)

                errori = predizioni - yRidotto

                self.theta = self.theta - self.learningRate * (1/batchSize) *np.dot(xRiodotto.T, errori)

            predizioniComplete = np.dot(X, self.theta)
            erroriCompleto = predizioniComplete - y

            thetaHistory[epoca] = self.theta
            costFunctionHistory[epoca] = (1/(2*m) * np.dot(erroriCompleto.T, erroriCompleto))



    def fit_sgd(self, X, Y):
        m = X.shape[0]

        thetaHistory = np.zerso((self.numeroIterate, self.numeroFeature))
        costFunctionHistory = self.np.zeros(self.numeroIterate)

        for epoca in range(0, self.numeroIterate):
            indiceCasuale = np.random.randint(m)

            x = X[indiceCasuale, :]
            y = Y[indiceCasuale]

            predizione = np.dot(x, self.theta)
            errore = predizione - y

            self.theta = self.theta - self.learningRate * np.dot(x.T, errore)

            predizioniComlete = np.dot(X, self.theta)
            erorriCompleti = predizioniComlete - Y

            thetaHistory[epoca] = self.theta
            costFunctionHistory[epoca] = (1/2*m) * np.dot(erorriCompleti.T, erorriCompleti)


#Funzione di costo della regressione Logistica
-(1/m) * (np.dot(y, np.log(predizioni)) + np.dot((1 - y), np.log(1 - predizioin)))
