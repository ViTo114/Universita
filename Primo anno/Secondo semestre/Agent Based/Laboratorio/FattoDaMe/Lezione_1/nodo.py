# Definiamo la classe che definisce la struttura dei nostri nodi
class Nodo:
    
    def __init__(self, stato, nodoGenitore, azione, costo):
        self.stato = stato
        self.genitore = nodoGenitore
        self.azione  = azione
        self.costo = costo
    
    
    def listaAzioni(self):
        if self.genitore == None:
            return []

        azioni = self.genitore.path()
        azioni.append(self.azione)

        return azioni
