from sklearn.svm import SVC

modello = SVC(kernel="linear", random_state=42)


from sklearn.decomposition import PCA

modello2 = PCA()

modello2.fit(X)

dati = modello2.

