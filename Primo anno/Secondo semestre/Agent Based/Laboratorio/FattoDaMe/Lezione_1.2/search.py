import random 

# Definiamo la nostra stratergia di ricerca
def randomSearch(starNode, endNode, problem):
    path = []

    if starNode.city == endNode.city:
        return [starNode]

    else:
        # Definiamo la nostra frontiera come una lista
        fringe = [starNode]

        while (True):
            node = random.choice(fringe)
            fringe.remove(node)

            path.append(node)

            neighborNode = node.expandNode(problem)
    
            for item in neighborNode:
                if (item.city == endNode.city):
                    path.append(item)
                    return path

                else:
                    fringe.append(item)
