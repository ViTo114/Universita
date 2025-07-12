from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
from sklearn.cluster import KMeans


class Kmidoid:
    def __init__(self, numeroCluster, randomState, distanza = euclidean_distances):
        self.numeroCluster = numeroCluster
        self.random = np.random.RandomState(randomState)
        self.distanza = distanza

        self.indici= []
        self.midoid = []

    def compute_cost(self,X, indici):
        yPred = np.argmin(self.distanza(X, X[indici, :]), axis=1)
        return np.sum([np.sum(self.distanza(X[yPred==i], X[[indici[i]], :])), for i in set(yPred)]), y_pred

    def fit(self, X):
        randomInt = self.random.randint()

        self.indici = [randomInt(X.shape[0])]

        for k in range(0, self.numeroCluster -1):
            possibiliMidoid = randomInt(X.shape[0])

            while possibiliMidoid in self.indici:
                possibiliMidoid = randomInt(X.shape[0])

            self.indici.append(possibileMidoid)

        self.midoid = X[self.indici]

        cost, _ = compute_cost(X, self.indici)
        yPred = np.argmin(self.distanza(X, self.midoid), axis=1)

        primaVolta = True

        newCost = cost
        newYpred = yPred.copy()
        newIndici = self.indici[:]

        while (newCost < cost) | primaVolta:
            primaVolta = False

            cost = newCost
            yPred = newYpred.copy()
            self.indici = newIndici[:]

            for k in range(0, self.numeroCluster):
                for r in [i for i, x in enumerate(newYpred==k) if x]:
                    if r not in self.indici:
                        tempInidci = self.indici[:]
                        tempInidci[k] = r
                        tempCost, tempCost = compute_cost(X, tempInidci)

                        if tempCost < newYpred:
                            newCost = tempCost
                            newYpred = tempYpred.copy()
                            newIndici = tempInidci[:]


        self.midoid = X[self.indici, :]


# Identificazione del numero di cluster con il metodo del gomito

wcss = []

rangeCluster = range(1, 12)

for cluster in rangeCluster:
    modello = Kmidoid()
    modello.fit()
    y_pred = modello.predict(dataset)


    wcss_locale = 0
    for k in range(0, cluster):
        clusterPoint = dataset[y_pred==k]

        distanza = np.sum((clusterPoint - modello.midoid[k])**2)

        wcss_locale = wcss_locale + distanza

    wcss.append(wcss_locale)


# Se io volessi usaer le libreiria

wcss2 = []

rangeCluster = range(1,11)

for cluster in rangeCluster:
    modello2 = KMeans()
    KMeans.fit(dataset)
    yPred = modello2.predict(dataset)

    wcss_locale = 0

    for k in range(0, cluster):
        wcss_locale = wcss_locale + modello2.inertia_

    wcss2.append(wcss_locale)