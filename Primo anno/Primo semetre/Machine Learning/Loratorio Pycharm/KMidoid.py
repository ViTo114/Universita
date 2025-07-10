import numpy as np

class KMidoid:
    def __init__(self, numeroCluster, distanza, randomState):
        self.numeroCluster = numeroCluster
        self.distanza = distanza
        self.random = np.random.RandomState(randomState)

        self.midoid = []
        self.indici = []


    def compute_cost(self, X, indici):
        y_pred = np.argmin(self.distanza(X, X[indici]), axis=1)

        return np.sum([np.sun(self.distanza(X[y_pred==i], X[[indici[i]], :])) for i in set(y_pred)]), y_pred


    def fit(self, X):
        randomInt = self.random.randint

        self.indici = [randomInt(X.shape[0])]

        for k in range(0, self.numeroCluster-1):
            possibileMidoid = randomInt(X.shape[0])

            while possibileMidoid in self.indici:
                possibileMidoid = randomInt(X.shape[0])

            self.indici.append(possibileMidoid)

        self.midoid = X[self.indici, :]

        y_pred = np.argmin(self.distanza(X, self.midoid), axis=1)

        cost, _ = compute_cost(X, self.indici)

        newCost = cost
        new_y_pred = y_pred.copy()
        newIndici = self.indici[:]

        primaVolta = True

        while (newCost < cost) | primaVolta:
            primaVolta = False

            cost = newCost
            self.indici = newIndici[:]
            y_pred = new_y_pred.copy()

            for k in range(self.numeroCluster):
                for r in [i for i, x in enumerate(new_y_pred == k) if x]:
                    if r not in self.indici:
                        tempIndici = self.indici[:]
                        tempIndici[k] = r
                        tempCost, temp_y_pred = compute_cost(X, tempIndici)

                        if tempCost < newCost:
                            newCost = tempCost
                            newIndici = tempIndici[:]
                            new_y_pred = temp_y_pred.copy()


        self.midoid = X[self.indici]