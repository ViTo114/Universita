from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
from  sklearn.cluster import KMeans

class Kmidoi:
    def __init__(self, numeroCluster, randomState, distanza=euclidean_distances):
        self.numeroCluster = numeroCluster
        self.distanza = distanza
        self.random = np.random.RandomState(randomState)

        self.indici = []
        self.midoid = []



    def compute_cost(self, X, indici):
        y_pred = np.argmin(self.distanza(X, X[indici, :]), axis=1)
        return np.sum([np.sum(self.distanza(X[i], X[[indici[i]], :])) for i in set(y_pred)]), y_pred


    def fit(self, X):
        randomInt = self.random.randint

        self.indici = X[randomInt(X.shape[0])]

        for k in range(0, self.numeroCentroidi):
            possibileMidoid = randomInt(X.shape[0])

            while possibileMidoid in self.indici:
                possibileMidoid = randomInt(X.shape[0])

            self.indici.append(possibileMidoid)


        self.midoid = X[self.indici, :]

        y_pred = np.argmin(self.distanza(X, self.midoid), axis=1)

        cost, _ = self.compute_cost(X, self.indici)

        primaVolta = True

        newCost = cost
        newYpred = y_pred.copy()
        newIndici = self.indici[:]

        while (newCost < cost) | primaVolta:
            primaVolta = False

            cost = newCost
            y_pred = newYpred.copy()
            self.indici = newIndici[:]

            for k in range(0, self.numeroCluster):
                for r in [i for i, x in enumerate(newYpred==k) if x]:
                    if r not in self.indici:
                        tempIndici = self.indici[:]
                        tempIndici[k] = r
                        tempCost, tempYpred = self.compute_cost(X, tempIndici)

                        if tempCost < newCost:
                            newCost = tempCost
                            newYpred = tempYpred.copy()
                            newIndici = tempIndici[:]

        self.midoid = X[self.indici]



    def predizioni(self, X):
        return np.argmin(self.distanza(X, self.midoid), axis=1)




########################################################################################################################

#DEFINIZIIONE DEL METODO DEL GOMITO



wcss = []

rangeDiCluster = range(1, 11)

for numeroCluster in rangeDiCluster:
    modello = Kmidoi(numeroCluster=numeroCluster, randomState=42)

    modello.fit(Xtrain)

    yPred = modello.predizioni(Xtest)

    for k in numeroCluster:
        wcss = 0

        clusterPoint = X[y_pred==k]

        if clusterPoint.size == 0:
            continue

        else:
            distanza = np.sum((clusterPoint - modello.midoid[k])**2)
            wcss = wcss + distanza

    wcss.appen(wcss)
#######################################################################################################################
#Proviamo a definire il metodo del gomito con la libreria di sklearn

wcss = []

rangeCluster = range(0, 11)

for numeroCluster in rangeCluster:
    modello2 = KMeans(n_clusters=numeroCluster, random_state=42)
    modello2.fit(X_train)
    y_pred = modello2.predict(X_test)

    for k in range(0, numeroCluster):
        wcss = 0

        distanza = modello2.inertia_

        wcss = wcss + distanza

    wcss.append(wcss)






