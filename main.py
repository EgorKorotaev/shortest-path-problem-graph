from Repository import Graph
from prettytable import PrettyTable


def main():
    graph = Graph()
    graph.read()
    graph.initialization(input('start: '), input('finish: '), input('a_coefficient: '))

    x = PrettyTable()
    x.field_names = ['алгоритм', 'путь', 'длинна', 'вес', 'итерации', 'время']
    x.add_row(graph.depth_first())
    x.add_row(graph.breadth_first())
    x.add_row(graph.hill_climbing())
    x.add_row(graph.british_museum())
    x.add_row(graph.branch_and_bound())
    x.add_row(graph.a_star())
    print(x)


if __name__ == '__main__':
    main()
