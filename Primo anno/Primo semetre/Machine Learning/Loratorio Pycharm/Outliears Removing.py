from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from sklearn.impute import SimpleImputer

class OutliersRemover(BaseEstimator, TransformerMixin):
    def __init__(self, paramentro):
        self.upperBound = []
        self.lowerBound = []

        self.parametro = paramentro


    def boundaryDetecto(self, X):
        q1 = np.percentile(X, 25)
        q3 = np.percentile(X, 75)

        riq = q3 - q1

        self.upperBound.appen(q3 + riq*self.parametro)
        self.lowerBound.appen(q1 - riq*self.paramentro)


    def fit(self, X, y=None):
        np.apply_along_axis(self.outliersDetecto, axis=1, arr=X)


    def trasform(self, X, y=None):
        for variabile in range(X.shape[1]):

            x = X[:, variabile]

            upperMask = x > self.upperBound
            lowerMask = x < self.lowerBound

            x[upperMask | lowerMask] = np.nan

            X[:, variabile] = x

        imputer = SimpleImputer(strategy="mean")

        X  = imputer.fit_transform(X)
