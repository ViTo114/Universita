
# Elenco di tutte le città che stiamo considenrando
ALTAMURA = "Altamura"
MODUGNO = "Modugno"
RUVO = "Ruvo"
CORATO = "Corato"
TRANI = "Trani"
BARLETTA = "Barletta"

# Elenco di tutte le azioni che si possono relizzare
GO_TO_ALTAMURA = "Go to Altamura"
GO_TO_MODUGNO = "Go to Modugno"
GO_TO_RUVO = "Go to Ruvo"
GO_TO_CORATO = "Go to Corato"
GO_TO_TRANI = "Go to Trani"
GO_TO_BARLETTA = "Go to Barletta"


# Definiamo la classe che constituisce il problema
class Problema:

    # Definiamo il costruttore della classe
    def __init__(self, nodoPartenza, nodoObiettivo):
        
        self.parteza = nodoPartenza
        self.destinazione = nodoObiettivo

        # Definiamo tutte le azioni disponibili per un nodo attravero un dizionario
        self.mappa = {
                    ALTAMURA : [GO_TO_MODUGNO, GO_TO_TRANI],
                    MODUGNO : [GO_TO_ALTAMURA, GO_TO_TRANI, GO_TO_RUVO],
                    RUVO : [GO_TO_MODUGNO, GO_TO_CORATO],
                    CORATO : [GO_TO_RUVO, GO_TO_CORATO],
                    TRANI : [GO_TO_ALTAMURA, GO_TO_MODUGNO, GO_TO_BARLETTA, GO_TO_CORATO],
                    BARLETTA : [GO_TO_RUVO, GO_TO_TRANI],
                     }

    # Restituisce le azioni disposinili per un possibile stato 
    def actions(self, stato):
        return self.mappa[stato]

    
    #  Restituisce il nodo di destinazoine data una certa azione 
    def moveTo (self, action):
        if action == GO_TO_ALTAMURA:
            return ALTAMURA

        elif action == GO_TO_CORATO:
            return CORATO

        elif action == GO_TO_MODUGNO:
            return MODUGNO

        elif action == GO_TO_RUVO:
            return RUVO

        elif action == GO_TO_TRANI:
            return TRANI

        elif action == GO_TO_BARLETTA:
            return BARLETTA
