import time

from algorithms.GraphSearchAlgorithm import GraphSearchAlgorithm


class DepthFirst(GraphSearchAlgorithm):

    def __init__(self, graph):
        super().__init__(graph)

    def run(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.graph.start])

        while True:
            if len(turn) == 0:
                return ['depth_first', '***', '***', '***', iteration, (time.time() - start_time)]
            elif turn[0][-1] == self.graph.finish:
                return ['depth_first', str(turn[0]), len(turn[0]), '***', iteration, (time.time() - start_time)]

            temp_Top = turn[0]
            turn.pop(0)

            for top in self.getPaths(temp_Top):
                turn.insert(0, top)
            iteration = iteration + 1
