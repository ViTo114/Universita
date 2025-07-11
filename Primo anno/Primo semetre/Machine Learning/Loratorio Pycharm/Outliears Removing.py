from sklearn.base import TransformerMixin, BaseEstimator
import numpy as np
from sklearn.impute import SimpleImputer

class OulierRemover(TransformerMixin, BaseEstimator):
    def __init__(self, parametro):
        self.parametro = parametro

        self.limiteSuperiore = []
        self.limiteInferiore = []


    def identificazioneLimiti(self, X):
        q1 = np.percentile(X, 25)
        q3 = np.percentile((x, 75))

        riq = q3 - q1

        self.limiteInferiore.append(q1 - self.parametro*riq)
        self.limiteSuperiore.append(q3 + self.parametro*riq)


    def fit(self, X, y=None):
        np.apply_along_axis(self.identificazioneLimiti, axis=1, arr=X)


    def transform(self, X, y=None):
        for variabile in X.shape[1]:
            x = X[:, variabile]

            upperMask = x > self.limiteSuperiore[variabile]
            lowerMask = x < self.limiteInferiore[variabile]

            x[upperMask | lowerMask] = np.nan

            X[:, variabile] = x


        imputer = SimpleImputer(strategy="mean")
        X = imputer.fit_transform(X)

        return X
