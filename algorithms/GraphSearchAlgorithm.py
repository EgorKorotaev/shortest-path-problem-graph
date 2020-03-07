from abc import ABC, abstractmethod


class GraphSearchAlgorithm(ABC):

    def __init__(self, graph):
        self.graph = graph

    def getPaths(self, path):
        raw_turn = []
        for branch in self.graph.graph[str(path[-1])].edges:
            path_extended = path.copy()
            new_vertex = branch['edgeName']
            path_extended.append(new_vertex)
            if new_vertex not in path:
                raw_turn.extend([path_extended])
        return raw_turn

    def removeDuplicateEndpoints(self, turn):
        turn.sort(key=self.keyCost)
        counting = {}
        for item in turn:
            if counting.get(str(item[len(item) - 1])) is None:
                counting[str(item[len(item) - 1])] = 0
            else:
                counting[str(item[len(item) - 1])] = counting[str(item[len(item) - 1])] + 1
        turn.reverse()
        for item in turn:
            if counting[str(item[len(item) - 1])] != 0:
                turn.remove(item)
                counting[str(item[len(item) - 1])] = counting[str(item[len(item) - 1])] - 1
        turn.reverse()
        return turn

    def keyCost(self, item):
        cost = 0
        for top in item:
            if item.index(top) + 1 < len(item):
                for edge in self.graph.graph[str(top)].edges:
                    if edge['edgeName'] == item[item.index(top) + 1]:
                        cost = cost + edge['weight']
        return cost

    @abstractmethod
    def run(self):
        pass
