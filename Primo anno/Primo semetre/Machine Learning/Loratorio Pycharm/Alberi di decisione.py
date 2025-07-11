from sklearn.tree import DecisionTreeClassifier

modello1 = DecisionTreeClassifier()
modello1.fit(Xtrain, Ytrain)
modello1.predict(XTest)


#Voglio usare la gridsearch
from sklearn.model_selection import GridSearchCV

modello2 = DecisionTreeClassifier(random_state=123)

grid = {
        "param1" : "stocazzo",
        "param2" : "frocio",
        "param3" : "zocndmemt"
}

gridSearch = GridSearchCV(modello2, grid, scoring="accuracy" , cv=5)

gridSearch.fit(Xtrain, Ytest)

miglioriParamentri = gridSearch.best_params_
migliorModello = gridSearch.best_estimator_