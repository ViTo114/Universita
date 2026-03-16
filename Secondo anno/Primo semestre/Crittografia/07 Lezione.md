# FUNZIONE DI EULERO
La funzione di Eulero associa a ogni numero naturale il numero di interi positivi minori di esso che sono relativamente primi con esso.

Sia $\phi: \mathbb{N} \to \mathbb{N}$ la funzione definita come: $$\phi(n) = \left| \{ a \in \mathbb{Z} : 1 \le a < n \text{ e } \gcd(a, n) = 1 \} \right|$$
==NOTA==: phi indica la funzione di Eulero



**PROPRIETA' DELLA FUNZIONE DI EULERO:**
- **Conteggio Invertibili:** La funzione $\phi(n)$ indica precisamente il numero di **elementi invertibili** all'interno dell'anello $\mathbb{Z}_n$.
- **Condizione di Invertibilità:**  Un elemento $a \in \mathbb{Z}_n$ possiede un inverso moltiplicativo se e solo se è coprimo con il modulo $n$: $$a \in \mathbb{Z}_n \text{ è invertibile } \iff \gcd(a, n) = 1$$



==TEOREMA==: Siano $m, n \in \mathbb{N}$ due numeri **primi tra loro**. Allora la funzione $\phi$ soddisfa la seguente proprietà: $$\gcd(m, n) = 1 \implies \phi(m \cdot n) = \phi(m) \cdot \phi(n)$$
==TEOREMA DI EULERO==:  Siano $a \in \mathbb{Z}$ e $n \in \mathbb{N}$ due interi coprimi tra loro. Allora vale la seguente relazione:  Se $\gcd(a, n) = 1$, allora: $$a^{\phi(n)} \equiv 1 \pmod n$$

