import time

from algorithms.GraphSearchAlgorithm import GraphSearchAlgorithm


class BreadthFirst(GraphSearchAlgorithm):

    def __init__(self, graph):
        super().__init__(graph)

    def run(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.graph.start])

        while True:
            if len(turn) == 0:
                return [0, iteration, 'breadth_first', '***', (time.time() - start_time)]
            elif turn[0][-1] == self.graph.finish:
                return ['breadth_first', turn[0], len(turn[0]), '***', iteration, (time.time() - start_time)]

            temp_Top = turn[0]
            turn.pop(0)

            turn.extend(self.getPaths(temp_Top))
            iteration = iteration + 1
