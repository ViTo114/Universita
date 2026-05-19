# Definiamo tutte le città della nostra mappa 
ALTAMURA = "ALTAMURA"
MODUGNO = "MODUGNO"
RUVO = "RUVO"
TRANI = "TRANI"
BARLETTA = "BARLETTA"
CORATO = "CORATO"

class Problem:

    def __init__(self):
        # Definiamo la mappa della città come un dizionario che contienie una lista di città addiacenti con il relativo costo
        self.map = {
                        ALTAMURA : [(MODUGNO,5), (TRANI, 7)],
                        MODUGNO : [(ALTAMURA,5), (TRANI,1), (RUVO,10)],
                        RUVO : [(MODUGNO,10), (CORATO,2), (BARLETTA,8)],
                        CORATO : [(TRANI,4), (RUVO,2)],
                        TRANI : [(ALTAMURA,7), (MODUGNO,1), (BARLETTA,3)],
                        BARLETTA : [(TRANI,3), (RUVO, 8)]
                   }


        # Definiamo la soluzione del problema con una lista di azione che devono essere fatte 
        self.solution = []



    def findNeighbor (self, city):
        neighbor = self.map[city]

        neighborList = []
        
        for element in neighbor:
            neighborList.append(element[0])

        return neighborList
