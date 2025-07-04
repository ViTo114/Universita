# REGRESSIONE LINEARE SEMPLICE

In questo esempio utilizzeremo una dataset con due variabili di in input (_Size_ e _Badrooms_) e una sola variabile target (_price_)

Il primo step è quello di importare le librerie che si sono utili:
`import numpy ad np`
`import pandas as pd`

Come prima cosa carichiamo il nostro dataset in una variabile sfruttando la libreria pandas. In particolare useremo:
`house = pd.read_csv("percorso_del_file)`

Successivamente normalizziamo i dati tramite la _z-score normalizzation_:
`mean = house.mean(axis=0)`
`std = house.std(axis=0)`
`house = (house - mean)/std    #Questo è il calcolo della noralizzazione dei dati`

_NOTA_: il paramento _axis_ specifica lungo quale colonna eseguire la media. Quindi per _axis=0_ si intende l'asse verticale (e quindi calcola la media per ogni colonna), per _axis=0_ si intende l'ass