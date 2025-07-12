from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

modello = DecisionTreeClassifier()
modello.fit(Xtrain)
preidizione = modello.predict(X)


#Se io volessi usare una grid dovrei usare
grid ={}
modello2 = DecisionTreeClassifier()
gridSearcher = GridSearchCV(modello2, grid, cv=5)

bestModel = gridSearcher.best_estimator_
bestParameter = gridSearcher.best_params_


#Se io volessi realizzare una randomForest
modello3 = RandomForestClassifier()
modello3.fit(Xtrain)
preidizione3 = modello3.predict(Xtest)