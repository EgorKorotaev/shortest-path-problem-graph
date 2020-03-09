from Top import Top
import json


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
