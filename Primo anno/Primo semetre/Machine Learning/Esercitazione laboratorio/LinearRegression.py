import numpy as np

class RegressioneLineare:

    def __init__(self, learningRate, numeroFeature, numeroDiIterazione, seed):
        self.learningRate = learningRate
        self.numeroIteraizoni = numeroDiIterazione
        self.numeroFeature = numeroFeature
        self.seed = seed

        #Imposto il seed per definire la riproducibilità delle operazioni casuali
        np.random.seed(self.seed)

        #Definisco il vettore dei pesi
        self.theta = np.random.rand(self.numeroFeature)


    def fit_fullBatch(self, x, y):
        #Vado a definire il numero di istanze a disposizione
        m = x.shape[0]

        #Definisco le cronologie dei pesi e della funzione di costo
        thetaHistory = np.zeros(self.numeroIteraizoni)
        costFunctionHistory = np.zeros(self.numeroIteraizoni, self.theta.shape[0])

        #Definisco il ciclo for della discesa del gradiente
        for epoca in range (0, self.numeroIteraizoni):
            predizioni = np.dot(x, self.theta)

            errori = y - predizioni

            gradiente = np.dot(x.T, errori)

            #Eseguo l'aggiornamento dei pesi
            self.theta = self.theta - self.learningRate * ((1/m) * gradiente)

            #Aggiorno la cronologia
            thetaHistory[epoca] = self.theta
            costFunctionHistory[epoca] = (1/(2*m)) * np.dot(errori.T, errori)


    def fit_miniBatch(self, x, y, batchSize):
        m = x.shape[0]

        thetaHistory = np.zeros(self.numeroIteraizoni, self.theta.shape[0])
        costFunctionHistory = np.zeros(self.numeroIteraizoni)

        for epoca in range (0, self.numeroIteraizoni):
            for indice in range(0, m, batchSize):
                xRidotto = x[indice:indice+batchSize, :]
                yRidotto = y[indice:indice+batchSize]

                predizioni = np.dot(xRidotto, self.theta)

                errori = y - predizioni

                gradiente = np.dot(xRidotto.T, errori)

                self.theta = self.theta - self.learningRate * ((1/m) * gradiente)


            predizini = np.dot(x, self.theta)
            errori = y - predizini

            costFunctionHistory[epoca] = (1/(2*m)) * np.dot(errori.T, errori)
            thetaHistory[epoca] = self.theta


            









