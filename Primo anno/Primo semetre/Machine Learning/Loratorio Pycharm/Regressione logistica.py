import numpy as np
from sklearn.linear_model import LogisticRegression



class RegressoioneLogistica:
    def __init__(self, numeroIterate, numeroVariabili, seed, learningRate):
        self.numeroIterate = numeroIterate
        self.numeroVariabili = numeroVariabili
        self.learningRate = learningRate

        self.seed = seed
        np.random.seed(seed)

        self.theta = np.random.rand(self.numeroVariabili)


    @staticmethod
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    def fit_fbgd(self, X, Y):
        m = X.shape[0]

        thetaHistory = np.zeros((self.numeroIterate, self.numeroVariabili))
        costFunctionHistory = np.zeros(self.numeroIterate)

        for epoca in range(0, self.numeroIterate):
            z = np.dot(X, self.theta)
            predizioni = self.sigmoid(z)

            errori = predizioni - y

            self.theta = self.theta - self.learningRate * (1/m) * np.dot(X.T, errori)

            thetaHistory[epoca] = self.theta
            costFunctionHistory[epoca] = (1/(2*m)) * np.dot(errori.T, errori)



modello = LogisticRegression(random_state=42)
modello.fit(X, Y)
