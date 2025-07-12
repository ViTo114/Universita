import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Caricamento dataset
dataset = pd.read_csv()

#Mescolamento delle istanze
dataset = dataset.sample(frac=-1, random_state=42).reset_index(drop=True)

#divisione delle feature
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]


#divionse in training e test
xTrain, xTest, yTrain, yTest = train_test_split(dataset, test_size=0.2, random_state=42)

#normalizzaione
scaler = StandardScaler()
xTrain = scaler.fit_transform(Xtrain)
xTest = scaler.transform(Xtest)


#aggiungere una colonna per il bias
xTrain.insert(0, "bias", 1)
xTest.insert(0, "bias", 1)