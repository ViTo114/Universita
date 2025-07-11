from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

class Kmeans:
    def __init__(self, numeroCluster, randomState, distanza=euclidean_distances):
        self.numeroCluster = numeroCluster
        self.distanza = distanza
        self.random = np.random.RandomState(randomState)

        self.centroidi = []


    def fit(self, X):
        randomInt = self.random.randint

        indici = X[randomInt(X.shape[0])]

        for k in range(0, self.numeroCluster -1):
            possibileCentroide = randomInt(X.shape[0])

            while possibileCentroide in indici:
                possibileCentroide = randomInt(X.shape[0])

        indici.append(possibileCentroide)

        self.centroidi = X[indici, :]

        condizione = True

        while condizione:
            vecchiCentroidi = self.centroidi.copy()

            y_pred = np.argmin(self.distanza(X, self.cetroidi), axis=1)

            for k in set(y_pred):
                self.centroidi[k] = np.mean(X[y_pred==k], axis=0)

            if vecchiCentroidi == self.centroidi:
                condizione = False


    def predizioni(self, X):
        return np.argmin(self.distan(X,self.centroidi))




