from Graph import Graph
from prettytable import PrettyTable

from algorithms.AStar import AStar
from algorithms.BranchAndBound import BranchAndBound


def main():
    graph = Graph()
    graph.read()
    graph.initialization(input('start: '), input('finish: '), input('a_coefficient: '))

    x = PrettyTable()
    x.field_names = ['алгоритм', 'путь', 'длинна', 'вес', 'итерации', 'время']

    algorithms = [BranchAndBound(graph), AStar(graph)]

    for algorithm in algorithms:
        x.add_row(algorithm.run())

    x.add_row(graph.depth_first())
    x.add_row(graph.breadth_first())
    x.add_row(graph.hill_climbing())
    x.add_row(graph.british_museum())
    print(x)


if __name__ == '__main__':
    main()
