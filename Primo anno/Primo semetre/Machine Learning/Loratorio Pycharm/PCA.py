import numpy as np
from sklearn.decomposition import PCA


modello = PCA(X.shape[1], random_state=42)

NewXtrain = modello.fit_transform(Xtrain)


varianza = np.var(NewXtrain, axis=1)
varianzaRatio = varianza / np.sum(varianza)

varianzaCumulativa = np.cumsum(varianzaRatio)

for i in len(varianzaCumulativa):
    if varianzaCumulativa > minimo and minimo==0:
        numeroComponeti = varianzaCumulativa[i]

