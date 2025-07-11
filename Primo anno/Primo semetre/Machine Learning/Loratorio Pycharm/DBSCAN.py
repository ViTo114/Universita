from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

modello = DBSCAN()
modello.fit(Xtrain)
y_pred = modello.labels_


#Se volgio calcolare il silohoutscore

silhouteScore = silhouette_score(Xtrain, y_pred)