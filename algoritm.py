import json
from termcolor import colored, cprint


class Test:
    graph_1 = {
        "0": [0],
        "1": [2, 3, 5],
        "2": [1, 4],
        "3": [1, 5, 6],
        "4": [2, 5, 8, 9],
        "5": [1, 3, 4, 7],
        "6": [3, 7, 8],
        "7": [5, 6, 12],
        "8": [4, 6, 10, 11, 12],
        "9": [4, 10],
        "10": [8, 9, 11, 15],
        "11": [8, 10, 12, 14],
        "12": [7, 8, 11, 13],
        "13": [12, 18],
        "14": [11, 15, 17],
        "15": [10, 14, 16, 17],
        "16": [15, 19],
        "17": [14, 15, 19, 21],
        "18": [13, 20],
        "19": [16, 17, 20],
        "20": [18, 19, 21],
        "21": [17, 18, 20]
    }
    graph_2 = {
        '1': [2, 9, 19],
        '2': [1, 3, 15],
        '3': [2, 4, 8],
        '4': [3, 5, 16],
        '5': [4, 6, 12],
        '6': [5, 7, 14],
        '7': [6, 8, 17],
        '8': [3, 7, 9],
        '9': [1, 8, 10],
        '10': [9, 11, 16],
        '11': [10, 12, 18],
        '12': [5, 11, 13],
        '13': [12, 14, 19],
        '14': [6, 13, 15],
        '15': [2, 14],
        '16': [4, 10, 17],
        '17': [7, 16, 18],
        '18': [11, 17, 19],
        '19': [1, 13, 18],
    }
    graph_3 = {
        'S': [10, 'A', 'D'],
        'A': [8, 'S', 'C', 'D'],
        'B': [6, 'B', 'C'],
        'C': [4, 'B'],
        'D': [7, 'S', 'A', 'E'],
        'E': [6, 'D', 'F'],
        'F': [3, 'E', 'G'],
        'G': [1, 'G'],
    }
    graph_4 = {
        'S': [['A', 3], ['D', 4]],
        'A': [['S', 3], ['B', 5], ['D', 4]],
        'B': [['A', 4], ['E', 5], ['C'], 4],
        'C': [['B', 4]],
        'D': [['S', 4], ['A', 5], ['E', 2]],
        'E': [['D', 2], ['B', 5], ['F', 4]],
        'F': [['E', 4], ['G', 3]],
        'G': [['F', 3]]
    }

    start = None
    finish = None
    outpu_to_the_screen = None
    output1 = None
    output2 = None
    graph = graph_1

    def out_red(text):
        print("\033[31m{}\033[0m".format(text))

    def out_green(text):
        print("\033[32m{}\033[0m".format(text))

    def out_blue(text):
        print("\033[34m{}\033[0m".format(text))

    @staticmethod
    def go2():
        start = input('\033[33mВведте начальное положение в графе: \033[0m')
        finish = int(input('\033[33mВведите искомую вершину графа: \033[0m'))
        outpu_to_the_screen = input('\033[33mОтображать промежуточные рещультаты? \033[0m')
        turn = []
        raw_turn = []
        iteration = 0

        while True:
            if outpu_to_the_screen == '0' or outpu_to_the_screen == 'да':
                print('\033[34m', *turn, '\033[0m', sep='\n')
                print('\033[33mколичество итераций: ', iteration, '\033[0m')
            if len(turn) == 0:
                print('\033[33mколичество итераций: ', iteration, '\033[0m')
                print('\033[33mПоиск в ширину вершина не достижима :-(\033[0m')
                return ''
            elif turn[0][len(turn[0]) - 1] == finish:
                print('\033[33mколичество итераций: ', iteration, '\033[0m')
                print('\033[33mНашли! Поиск в ширину путь:', turn[0], ' длинной в', len(turn[0]), '\033[0m')
                return turn[0]

            temp_Top = turn[0]
            turn.pop(0)

            pointer = Test.graph_3[str(temp_Top[len(temp_Top) - 1])]
            for branch in pointer:
                # if path[len(path) - 2] != branch:
                temp_turn = temp_Top.copy()
                # print(temp_turn, "q")
                temp_turn.append(branch)
                number_of_repetitions = 0
                for top in temp_turn:
                    if temp_turn.count(top) == 1:
                        number_of_repetitions = number_of_repetitions + 1
                if number_of_repetitions == len(temp_turn):
                    if outpu_to_the_screen == '0' or outpu_to_the_screen == 'да':
                        Test.out_green(temp_turn)
                    raw_turn.extend([temp_turn])
                elif len(temp_turn) >= 3 and temp_turn[len(temp_turn) - 3] != temp_turn[len(temp_turn) - 1]:
                    if outpu_to_the_screen == '0' or outpu_to_the_screen == 'да':
                        Test.out_red(temp_turn)
                    # pass
                # print(raw_turn)

            turn.reverse()
            raw_turn.reverse()
            turn.extend(raw_turn)
            turn.reverse()
            raw_turn.clear()

            iteration = iteration + 1

    @staticmethod
    def go():
        Test.start = input('\033[33mВведте начальное положение в графе: \033[0m')
        Test.finish = int(input('\033[33mВведите искомую вершину графа: \033[0m'))
        Test.outpu_to_the_screen = input('\033[33mОтображать промежуточные рещультаты? \033[0m')
        Test.test1()
        Test.test2()

    @staticmethod
    def test2():
        # graph = json.load(open(r'test.json', 'r', encoding="utf-8"))
        # turn = [[0, 0]]
        start = Test.start
        finish = Test.finish
        outpu_to_the_screen = Test.outpu_to_the_screen

        turn = []
        raw_turn = []
        iteration = 0
        turn.append([int(start)])

        while True:
            if outpu_to_the_screen == '0' or outpu_to_the_screen == 'да':
                print('\033[34m', *turn, '\033[0m', sep='\n')
                print('\033[33mколичество итераций: ', iteration, '\033[0m')
            if len(turn) == 0:
                print('\033[33mколичество итераций: ', iteration, '\033[0m')
                print('\033[33mПоиск в ширину вершина не достижима :-(\033[0m')
                return ''
            elif turn[0][len(turn[0]) - 1] == finish:
                print('\033[33mколичество итераций: ', iteration, '\033[0m')
                print('\033[33mНашли! Поиск в ширину путь:', turn[0], ' длинной в', len(turn[0]), '\033[0m')
                return turn[0]

            temp_Top = turn[0]
            turn.pop(0)

            pointer = Test.graph[str(temp_Top[len(temp_Top) - 1])]
            for branch in pointer:
                # if path[len(path) - 2] != branch:
                temp_turn = temp_Top.copy()
                # print(temp_turn, "q")
                temp_turn.append(branch)
                number_of_repetitions = 0
                for top in temp_turn:
                    if temp_turn.count(top) == 1:
                        number_of_repetitions = number_of_repetitions + 1
                if number_of_repetitions == len(temp_turn):
                    if outpu_to_the_screen == '0' or outpu_to_the_screen == 'да':
                        Test.out_green(temp_turn)
                    raw_turn.extend([temp_turn])
                elif len(temp_turn) >= 3 and temp_turn[len(temp_turn) - 3] != temp_turn[len(temp_turn) - 1]:
                    if outpu_to_the_screen == '0' or outpu_to_the_screen == 'да':
                        Test.out_red(temp_turn)
                    # pass
                # print(raw_turn)

            turn.reverse()

            raw_turn.reverse()
            turn.extend(raw_turn)
            turn.reverse()
            raw_turn.clear()

            iteration = iteration + 1

    @staticmethod
    def test1():
        # graph = json.load(open(r'test.json', 'r', encoding="utf-8"))
        # turn = [[0, 0]]
        start = Test.start
        finish = Test.finish
        outpu_to_the_screen = Test.outpu_to_the_screen

        turn = []
        raw_turn = []
        iteration = 0
        turn.append([int(start)])

        while True:
            if outpu_to_the_screen == '0' or outpu_to_the_screen == 'да':
                print('\033[34m', *turn, '\033[0m', sep='\n')
                print('\033[33mколичество итераций: ', iteration, '\033[0m')
            if len(turn) == 0:
                print('\033[33mколичество итераций: ', iteration, '\033[0m')
                print('\033[33mПоиск в глубину вершина не достижима :-(\033[0m')
                return ''
            elif turn[0][len(turn[0]) - 1] == finish:
                print('\033[33mколичество итераций: ', iteration, '\033[0m')
                print('\033[33mНашли! Поиск в глубину путь:', turn[0], ' длинной в', len(turn[0]), '\033[0m')
                return turn[0]

            temp_Top = turn[0]
            turn.pop(0)

            pointer = Test.graph[str(temp_Top[len(temp_Top) - 1])]
            for branch in pointer:
                # if path[len(path) - 2] != branch:
                temp_turn = temp_Top.copy()
                # print(temp_turn, "q")
                temp_turn.append(branch)
                number_of_repetitions = 0
                for top in temp_turn:
                    if temp_turn.count(top) == 1:
                        number_of_repetitions = number_of_repetitions + 1
                if number_of_repetitions == len(temp_turn):
                    if outpu_to_the_screen == '0' or outpu_to_the_screen == 'да':
                        Test.out_green(temp_turn)
                    raw_turn.extend([temp_turn])
                elif len(temp_turn) >= 3 and temp_turn[len(temp_turn) - 3] != temp_turn[len(temp_turn) - 1]:
                    if outpu_to_the_screen == '0' or outpu_to_the_screen == 'да':
                        Test.out_red(temp_turn)
                    # pass
                # print(raw_turn)

            turn.extend(raw_turn)
            raw_turn.clear()

            iteration = iteration + 1


Test.go()
