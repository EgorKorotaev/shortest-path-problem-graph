import time

from algorithms.GraphSearchAlgorithm import GraphSearchAlgorithm


class AStar(GraphSearchAlgorithm):

    def __init__(self, graph):
        super().__init__(graph)

    def a_star(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.graph.start])

        while True:
            if len(turn) == 0:
                return [0, iteration, 'hill_climbing', (time.time() - start_time)]
            elif turn[0][-1] == self.graph.finish:
                return ['a_star', turn[0], len(turn[0]), self.keyCost(turn[0]), iteration, (time.time() - start_time)]

            temp_Top = turn[0]
            turn.pop(0)

            turn.extend(self.getPaths(temp_Top))
            turn = self.removeDuplicateEndpoints(turn)

            def keyA(item):
                return self.keyCost(item) + (
                        self.graph.a_coefficient * self.graph.graph[str(item[-1])].heuristicEvaluation)

            turn.sort(key=keyA)

            iteration = iteration + 1
