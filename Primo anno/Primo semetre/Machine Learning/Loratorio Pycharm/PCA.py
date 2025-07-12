from sklearn.decomposition import PCA
import numpy as np

pca = PCA(n_components="numeroOriginali", random_state=42)

pca.fit_transform(Xtrain)

varianza = np.var(Xtrain, axis=0)

varianzaRatio = varianza /np.sum(varianza)

varainzaCumulativa = np.cumsum(varianzaRatio)

