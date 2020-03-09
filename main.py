from Graph import Graph
from prettytable import PrettyTable

from algorithms.AStar import AStar
from algorithms.BranchAndBound import BranchAndBound
from algorithms.BritishMuseum import BritishMuseum
from algorithms.HillClimbing import HillClimbing
from algorithms.DepthFirst import DepthFirst
from algorithms.BreadthFirst import BreadthFirst


def main():
    graph = Graph()
    graph.read()
    graph.initialization(input('start: '), input('finish: '), input('a_coefficient: '))

    x = PrettyTable()
    x.field_names = ['алгоритм', 'путь', 'длинна', 'вес', 'итерации', 'время']

    algorithms = [BreadthFirst(graph), DepthFirst(graph), HillClimbing(graph), BritishMuseum(graph), BranchAndBound(graph), AStar(graph)]

    for algorithm in algorithms:
        x.add_row(algorithm.run())

    print(x)


if __name__ == '__main__':
    main()
