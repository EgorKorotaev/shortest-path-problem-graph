import time

from algorithms.GraphSearchAlgorithm import GraphSearchAlgorithm


class BritishMuseum(GraphSearchAlgorithm):

    def __init__(self, graph):
        super().__init__(graph)

    def run(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.graph.start])
        end_turn = []

        while True:
            if len(turn) == 0:
                if len(end_turn) == 0:
                    return [0, iteration, 'british_museum', (time.time() - start_time)]
                else:
                    end_turn.sort(key=self.keyCost)
                    return ['british_museum', end_turn[0], len(end_turn[0]), self.keyCost(end_turn[0]), iteration,
                            (time.time() - start_time)]

            if turn[0][len(turn[0]) - 1] == self.graph.finish:
                end_turn.append(turn[0])

            temp_Top = turn[0]
            turn.pop(0)

            turn.extend(self.getPaths(temp_Top))

            iteration = iteration + 1
