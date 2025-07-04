# REGRESSIONE LINEARE SEMPLICE

In questo esempio utilizzeremo una dataset con due variabili di in input (_Size_ e _Badrooms_) e una sola variabile target (_price_)


Il primo step è quello di importare le librerie che si sono utili:
`import numpy ad np`
`import pandas as pd`


Come prima cosa carichiamo il nostro dataset in una variabile sfruttando la libreria pandas. In particolare useremo:
`houses = pd.read_csv("percorso_del_file)`


Andiamo a mischiare le istanze (non ho ancora capito per quale motivo):
`houses = houses.sample(frac=1, random_state=123).reset_index(drop=True)`


Successivamente normalizziamo i dati tramite la _z-score normalizzation_:
`mean = houses.mean(axis=0)`
`std = houses.std(axis=0)`
`houses = (house - mean)/std    #Questo è il calcolo della noralizzazione dei dati`

_NOTA_: il paramento _axis_ specifica lungo quale colonna eseguire la media. Quindi per _axis=0_ si intende l'asse verticale (e quindi calcola la media per ogni colonna), per _axis=0_ si intende l'asse verticale e calcola la media per ogni riga


Successivamente andiamo a dividere il dataset in due varibili:
`x = houses[:,0]`
`y = house[:, 1]`


Successivamente andiamo a aggiungere un colonna di soli 1, per definire un valore da associare a bias:
`x = np.c_[np.ones(x.shape[0]), x ]`



Infine andiamo a sfruttare una classe definita da noi prece
