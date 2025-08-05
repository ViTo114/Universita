Una gramamtica di tipo 2 è una quadrupla del tipo **_(T, N, S, P)_** dove:
- **T** è l'insieme dei simboli terminali
- **N** è l'insieme dei simboli non terminali 
- **S** è il simbolo inziale
- **P** è l'insieme delle regole di produzione

In questa tipologia di grammatica le regole di produzione sono della forma $A \rightarrow \alpha$. dove $A$ rappresenta un simbolo non terminale e prende il nome di **TESTA**, mentre $\alpha$ rappresenta una qualunque sequenza di terminali e non terminali e prende il nome di **CORPO** della regola.

L'obiettivo principale di una produzione della grammatica è di generare stringhe di terminali chiamate **frasi** del linguaggio definito dalla grammatica.

Il processo di derivazione delle stringhe può avvenire tramite la derivazione (partendo dal simbolo di partenza) oppure tramite **ALBERI DI DERIVAZIONE**
==NOTA: entrambi i metodi derivano le stesse stringhe



# DEFINIZIONI
Il linguaggio generata da una grammatica partendo da un non-terminale $A$ (che è diverso dal simbolo di partenza $S$ ) viene indicato con **$L_A(G)$

Mentre il linguaggio generato da partendo dal simbolo di partenza $S$ viene indicato con $L(G)$


Un linguaggio si dice **CONTEXT-FREE** se esiste una grammatica context free che lo generata.

Una derivazione è detta **RICORSIVA** se partendo da un non terminale, produce in almeno un passo una stringa che contiene no stesso non terminale:
![image.png](data:image/png;base64,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)


Se $\alpha = \varepsilon$ allora si parlerà di **RICORSIONE DA SINISTRA**, altrimenti se $\beta = \varepsilon$ si parlerà di **RICORSIONE DA DESTRA**.
In ogni caso il simbolo non terminale $A$ si chiamerà **RICORSIVO**

