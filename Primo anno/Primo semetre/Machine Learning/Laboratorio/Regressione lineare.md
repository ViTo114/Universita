# REGRESSIONE LINEARE SEMPLICE

In questo esempio utilizzeremo una dataset con due variabili di in input (_Size_ e _Badrooms_) e una sola variabile target (_price_)

Il primo step è quello di importare le librerie che si sono utili:
`import numpy ad np`
`import pandas as pd`

Come prima cosa carichiamo il nostro dataset in una variabile sfruttando la libreria pandas. In particolare useremo:
`houses = pd.read_csv("percorso_del_file)`

Successivamente normalizziamo i dati tramite la _z-score normalizzation_:
`mean = houses.mean(axis=0)`
`std = houses.std(axis=0)`
`houses = (house - mean)/std    #Questo è il calcolo della noralizzazione dei dati`

_NOTA_: il paramento _axis_ specifica lungo quale colonna eseguire la media. Quindi per _axis=0_ si intende l'asse verticale (e quindi calcola la media per ogni colonna), per _axis=0_ si intende l'asse verticale e calcola la media per ogni riga


Successivamente andiamo a dividere il dataset in due varibili:
`x = houses[:,0]`
`y = house[:, 1]`






Il prossimo step è quello di aggiungere un colonna, che contiene in tutte le righe il valore 1, per associare un valore a bias

