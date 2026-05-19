import node
import problem
import search

problema = problem.Problem()

nodoPartenza = node.Node(problem.ALTAMURA, 0)
nodoDestinazione = node.Node(problem.RUVO, None)

percorso = search.randomSearch(nodoPartenza, nodoDestinazione, problema)

for citta in percorso:
    if (citta.city != nodoDestinazione.city):
        print(citta.city + " --> ")

    else:
        print(citta.city)
