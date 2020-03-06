class edges:
    def __init__(self):
        pass


class Top:
    def __init__(self, topName, heuristicEvaluation=None):
        self.topName = topName
        self.heuristicEvaluation = int(heuristicEvaluation)
        self.edges = []
        self.id = 0

    def addEdges(self, edgeName, weight):
        self.edges.append(
            {'edgeName': edgeName, 'weight': int(weight), 'id': self.id}
        )
        self.id = self.id + 1

    def removeEdges(self, edgeName):
        for edge in self.edges:
            if edge['edgeName'] == edgeName:
                self.edges.remove(edge)
