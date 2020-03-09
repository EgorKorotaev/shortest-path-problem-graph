import time

from algorithms.GraphSearchAlgorithm import GraphSearchAlgorithm


class HillClimbing(GraphSearchAlgorithm):

    def __init__(self, graph):
        super().__init__(graph)

    def run(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.graph.start])

        while True:
            if len(turn) == 0:
                return [0, iteration, 'hill_climbing', '***', (time.time() - start_time)]
            elif turn[0][-1] == self.graph.finish:
                return ['hill_climbing', turn[0], len(turn[0]), '***', iteration, (time.time() - start_time)]

            temp_Top = turn[0]
            turn.pop(0)

            turn.extend(self.getPaths(temp_Top))

            def keyEvaluation(item):
                return self.graph.graph[str(item[-1])].heuristicEvaluation

            turn.sort(key=keyEvaluation)
            iteration = iteration + 1
