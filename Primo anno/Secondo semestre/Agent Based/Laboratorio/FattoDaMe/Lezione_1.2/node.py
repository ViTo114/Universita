
class Node:
    
    def __init__(self, city, cost):
        self.city = city
        self.cost = cost                 # Il costo totale per raggiungere il nodo


    def expandNode(self, problem):
        neighbroCity = problem.map[self.city]

        neighbornNode = []

        for item in neighbroCity:
            neighbornNode.append(Node(item[0], self.cost+item[1])) 
        
        return neighbornNode


