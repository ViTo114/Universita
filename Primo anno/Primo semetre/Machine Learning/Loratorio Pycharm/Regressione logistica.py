import numpy as np

class LogisticRegression:
    def __init__(self, learningRate, numeroIterate, numeroFeature, seed):
        self.learningRate = learningRate
        self.numeroIterate = numeroIterate
        self.numeroFeature = numeroFeature
        self.seed = seed

        #Impostazione del seed casuale
        np.random.seed(self.seed)

        #Definizone del vettore dei pesi
        self.theta = np.random.rand(self.numeroFeature)


    @staticmethod
    def sigmoid (z):
        return 1 / (1 + np.exp(-z))


    def fullBatch_fit(self, X, Y):
        m = X.shape[0]

        thetaHistory = np.zeros((self.numeroIterate, self.theta.shape[0]))
        costFunctionHisoty = np.zeros(self.numeroIterate)

        for epoca in range(0, self.numeroIterate):
            z = np.dot(X, self.theta)

            predizioni = self.sigmoid(z)

            errori = predizioni - Y

            self.theta = self.theta - self.learningRate * 1/m * np.dot(X.T, errori)

            thetaHistory[epoca] = thetaHistory
            costFunctionHisoty[epoca] = -(1/m) * (np.dot(Y, np.log(predizioni)) + np.dot(1-Y, np.log(1 - predizioni)))



    def predizione(self, X, threshold):
        z = np.dto(X, self.theta)

        predizione = self.sigmoid(z)

        return predizione > threshold
