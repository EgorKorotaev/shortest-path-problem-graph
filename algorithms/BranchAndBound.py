import time

from algorithms.GraphSearchAlgorithm import GraphSearchAlgorithm


class BranchAndBound(GraphSearchAlgorithm):

    def __init__(self, graph):
        super().__init__(graph)

    def run(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.graph.start])

        while True:
            if len(turn) == 0:
                return [0, iteration, 'hill_climbing', (time.time() - start_time)]
            elif turn[0][-1] == self.graph.finish:
                return ['branch_and_bound', turn[0], len(turn[0]), self.keyCost(turn[0]), iteration,
                        (time.time() - start_time)]

            temp_Top = turn[0]
            turn.pop(0)

            turn.extend(self.getPaths(temp_Top))
            turn = self.removeDuplicateEndpoints(turn)
            iteration = iteration + 1
