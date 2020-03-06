from Top import Top
import json
import time


class Graph:

    graph = {}
    start = None
    finish = None

    def read(self):
        for raw_top in json.load(open(r'data.json', 'r', encoding="utf-8")):
            self.graph[raw_top['topName']] = Top(raw_top['topName'], raw_top['heuristicEvaluation'])
            for raw_edges in raw_top['edges']:
                self.graph[raw_top['topName']].addEdges(raw_edges['edgeName'], raw_edges['weight'])

    def initialization(self, start, finish, a_coefficient):
        self.start = start
        self.finish = finish
        self.a_coefficient = float(a_coefficient)

    def repeatedPartAll(self, temp_Top):
        raw_turn = []
        for branch in self.graph[str(temp_Top[len(temp_Top) - 1])].edges:
            temp_turn = temp_Top.copy()
            temp_turn.append(branch['edgeName'])
            number_of_repetitions = 0
            for top in temp_turn:
                if temp_turn.count(top) == 1:
                    number_of_repetitions = number_of_repetitions + 1
            if number_of_repetitions == len(temp_turn):
                raw_turn.extend([temp_turn])
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
                for edge in self.graph[str(top)].edges:
                    if edge['edgeName'] == item[item.index(top) + 1]:
                        cost = cost + edge['weight']
        return cost

    def depth_first(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.start])

        while True:
            if len(turn) == 0:
                return ['depth_first', '***', '***', '***', iteration, (time.time() - start_time)]
            elif turn[0][len(turn[0])-1] == self.finish:
                return ['depth_first', str(turn[0]), len(turn[0]), '***', iteration, (time.time() - start_time)]

            temp_Top = turn[0]
            turn.pop(0)

            for top in self.repeatedPartAll(temp_Top):
                turn.insert(0, top)
            iteration = iteration + 1

    def breadth_first(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.start])

        while True:
            if len(turn) == 0:
                return [0, iteration, 'breadth_first', '***', (time.time() - start_time)]
            elif turn[0][len(turn[0]) - 1] == self.finish:
                return ['breadth_first', turn[0], len(turn[0]), '***', iteration, (time.time() - start_time)]

            temp_Top = turn[0]
            turn.pop(0)

            turn.extend(self.repeatedPartAll(temp_Top))
            iteration = iteration + 1

    def hill_climbing(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.start])

        while True:
            if len(turn) == 0:
                return [0, iteration, 'hill_climbing', '***', (time.time() - start_time)]
            elif turn[0][len(turn[0]) - 1] == self.finish:
                return ['hill_climbing', turn[0], len(turn[0]), '***', iteration, (time.time() - start_time)]

            temp_Top = turn[0]
            turn.pop(0)

            turn.extend(self.repeatedPartAll(temp_Top))

            def keyEvaluation(item):
                return self.graph[str(item[len(item) - 1])].heuristicEvaluation

            turn.sort(key=keyEvaluation)
            iteration = iteration + 1

    def british_museum(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.start])
        end_turn = []

        while True:
            if len(turn) == 0:
                if len(end_turn) == 0:
                    return [0, iteration, 'british_museum', (time.time() - start_time)]
                else:
                    end_turn.sort(key=self.keyCost)
                    return ['british_museum', end_turn[0], len(end_turn[0]), self.keyCost(end_turn[0]), iteration, (time.time() - start_time)]


            if turn[0][len(turn[0]) - 1] == self.finish:
                end_turn.append(turn[0])

            temp_Top = turn[0]
            turn.pop(0)

            turn.extend(self.repeatedPartAll(temp_Top))

            iteration = iteration + 1

    def branch_and_bound(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.start])

        while True:
            if len(turn) == 0:
                return [0, iteration, 'hill_climbing', (time.time() - start_time)]
            elif turn[0][len(turn[0]) - 1] == self.finish:
                return ['branch_and_bound', turn[0], len(turn[0]), self.keyCost(turn[0]), iteration, (time.time() - start_time)]

            temp_Top = turn[0]
            turn.pop(0)

            turn.extend(self.repeatedPartAll(temp_Top))
            turn = self.removeDuplicateEndpoints(turn)
            iteration = iteration + 1

    def a_star(self):
        start_time = time.time()
        turn = []
        iteration = 0
        turn.append([self.start])

        while True:
            if len(turn) == 0:
                return [0, iteration, 'hill_climbing', (time.time() - start_time)]
            elif turn[0][len(turn[0]) - 1] == self.finish:
                return ['a_star', turn[0], len(turn[0]), self.keyCost(turn[0]), iteration, (time.time() - start_time)]

            temp_Top = turn[0]
            turn.pop(0)

            turn.extend(self.repeatedPartAll(temp_Top))
            turn = self.removeDuplicateEndpoints(turn)

            def keyA(item):
                return self.keyCost(item) + (self.a_coefficient * self.graph[str(item[len(item) - 1])].heuristicEvaluation)
            turn.sort(key=keyA)

            iteration = iteration + 1
