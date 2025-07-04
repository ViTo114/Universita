# REGRESSIONE LINEARE 


## DEFINIZIONE DEL FILE MAIN
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

==_NOTA_: il paramento _axis_ specifica lungo quale colonna eseguire la media. Quindi per _axis=0_ si intende l'asse verticale (e quindi calcola la media per ogni colonna), per _axis=0_ si intende l'asse verticale e calcola la media per ogni riga


Successivamente andiamo a dividere il dataset in due variabili:
`x = houses[:,0]`
`y = house[:, 1]`


Successivamente andiamo a aggiungere un colonna di soli 1, per definire un valore da associare a bias:
`x = np.c_[np.ones(x.shape[0]), x ]`


Infine andiamo a sfruttare una classe definita da noi precedentemente (vedremo dopo come è fatta questa classe) per addestrare il modello di regressione lineare:
`linear = LinearRegression(n_features=x.shape[1], n_steps=1000, learning_rate=0.01)`




## DEFINIZIONE DELLA CLASSE LINEARE REGRESSION
Per la definizione della nostra classe come prima cosa andiamo ad importare le libreria che ci saranno utili:
`import numpy as np`

### DEFINIZIONE DELLA CLASSE
Successivamente iniziamo a definire la classe con la seguente sintassi:
`class LinearRegression:`

### DEFINIZIONE DEL COSTRUTTORE
All'interno di questa classe (quindi andando a capo e scrivendo con un tab verso destra) andiamo a definire il costruttore del nostro oggetto (in questo caso della funzione lineare):
`def __init__(self, learning_rate=1e-2, n_steps=200, n_features=1, lmd=0.01, seed=123):

==_NOTA_: il parametro _lmd_ indica il valore del parametro di regolarizzazione usato nella tecnica di regularizzation==


Andiamo a definire le variabili che compongono questo oggetto:
`self.seed = seed
`p.random.seed(self.seed)`

`self.learning_rate = learning_rate`
`self.n_steps = n_steps`
`self.theta = np.random.rand(n_features)`
`self.lmd = lmd`

`#Creaiamo un vettore di n_feature, dove ogni campo ha il valore lmd`
`self.lmd_ = np.full(n_features, lmd)`
`self.lmd_ = lmd_[0]=0`

==_NOTA_: Nelle due ultime righe andiamo a definire una nuova variabile "lmd_"


### DEFINIZIONE DELLE FUNZIONI DI ADDESTRAMENTO
Con queste righe di codice appena mostrate terminiamo la definizione del costruttore della nostra classe. Ora dobbiamo definire il metodo che ci permette di addestrare il modello:
`def fit_fbgd(self, X_train, y_train):`

==_NOTA_: Questa funziona definisce l'addestramento del modello basato dul full batch gradiente descent==


In questa nuova funzione andiamo a definire tre nove variabili:
`#Memorizza il valore della funzione di costo in ogni iterata`
`cost_history = np.zeros(self.n_steps)  

`#Memorizza il valore dei paramenti ad ogni iterata`
`theta_history= np.zeros((self.n_steps, self.theta.shape[0]))

`#Definisce il numero di esempi di training`
`m=len(X_train)`


Successivamente andiamo a definire il ciclo for che rappresenta l'algoritmo di discesa del gradiente:
![[Pasted image 20250704163013.png]]

E possibile modificare questo ciclo for per sfruttare anche la regolarizzazione:
![[Pasted image 20250704163716.png]]


Al termine di entrambe queste due funzioni adiamo a ritornare sia la variabile cost_history che la variabile theta_history


Se Invece della full batch, volessi usare la stochastic gradiente descent
