import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("percorso file")

dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)

x = dataset.iloc[:, :-1]
y = dataset[:, -1]

indiceSplit = round(len(x)*0.8)
xTrain = x[:indiceSplit, :]
xTest = x[indiceSplit, :]
yTrain = y[:indiceSplit]
yTest = y[:indiceSplit]

xTrain, xTest, yTrain, yTest = train_test_split(x,y, random_state=42, test_size=0.2)


media = xTrain.mean(axis=0)
deviazione = xTrain.std(axis=0)
xTrain = (xTrain - media) / deviazione
xTest = (xTest - media) / deviazione

scaler = StandardScaler()
xTrain = scaler.fit_transform(xTrain)
xTest = scaler.transform(xTest)


xTrain.insert(0, "bias", 1)
xTest.insert(0, "bias", 1)




