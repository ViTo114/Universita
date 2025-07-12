import numpy as np
from sklearn.impute import SimpleImputer


class OutlierRemove:
    def __init__(self, paramentro):
        self.parametro = paramentro

        self.limiteSuperiore = []
        self.limiteInferiore = []


    def identificazioneLimiti(self, X):
        q1 = np.percetile(X, 25)
        q3 = np.percentile(X, 75)

        riq = q3 -q1

        self.limiteInferiore.append(q1 - riq*self.parametro)
        self.limiteSuperiore.append(q3 + riq*self.parametro)


    def fit(self, X):
        np.apply_along_axis(self.identificazioneLimiti, axis=1, arr=X)


    def trasform(self, X):
        for varibile in X.shape[1]:
            x = X[:, varibile]

            upperMask = x > self.limiteSuperiore[varibile]
            lowerMask = x < self.limiteInferiore[varibile]

            x[upperMask | lowerMask] = np.nan

            X[:, varibile] = x


        imputer = SimpleImputer(strategy="mean")
        imputer.fit_transform(X)


