from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

modello = DecisionTreeClassifier(criterion="entropy", max_depth=5, min_samples_leaf=7, random_state=42)
modello.fit(X,y)

grid ={
        "criterion" : "entropy",
        "max_depht" : [1, 2, 3, 4],
        "min_sample_leaf" : [1, 2, 3],
}

modello = DecisionTreeClassifier(random_state= 42)
ricercaGrid = GridSearchCV(estimator=modello, param_grid=grid, cv=5 )


ricercaGrid.fit(X,Y)

ricercaGrid.best_params_
ricercaGrid.best_estimator_
