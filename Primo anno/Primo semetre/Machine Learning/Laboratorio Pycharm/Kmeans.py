import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

class Kmeans:
    def __init__(self, numeroCluser, randomState, distance=euclidean_distances):
        self.numeroCluster = numeroCluser
        self.random = np.random.RandomState(randomState)
        self.distance = distance

        self.centroidi = []


    def fit(self, X):
        radomInt = self.random.randint

        indici = [radomInt(X.shape[0])]

        for k in range(0, self.numeroCluster-1):
            possibileCentroide = radomInt(X.shape[0])

            while possibileCentroide in indici:
                possibileCentroide = radomInt(X.shape[0])

            indici.append(possibileCentroide)

        self.centroidi = X[indici, :]

        condizione= True

        while condizione:
            vecchiCentroidi = self.centroidi.copy()

            yPred = np.argmin(self.distanza(X, self.centroidi),axis=1)

            for k in set(yPred):
                self.centroidi[k] = np.mean(X[yPred==k], axis=0)

            if vecchiCentroidi == self.centroidi:
                condizione = False


    def preidizione(self, X):
        return np.argmin(self.distanza(X, self.indici), axis=1)

