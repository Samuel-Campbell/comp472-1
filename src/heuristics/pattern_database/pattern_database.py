from itertools import permutations
from util.file import File
from sys import stdout
from game_builder.board.game_board import GameBoard


class PatternDatabase:
    def __init__(self):
        self.pattern_dictionary = {}

    def find_patterns(self):
        pattern_1 = list(set(permutations([0, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 5)))
        pattern_2 = list(set(permutations([0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, -1, -1, -1, -1], 5)))

        unsolved_dictionary = {}
        solved_dictionary = {}

        self.create_patterns(pattern_1, [1, 2, 0], unsolved_dictionary)
        self.create_patterns(pattern_2, [1, 0, 10], solved_dictionary)
        self.merge_patterns(solved_dictionary, unsolved_dictionary)

    def create_patterns(self, single_row_pattern, variable_count, dictionary):
        dual_row_pattern = []
        for i in range(len(single_row_pattern)):
            for j in range(len(single_row_pattern)):
                dual_row_pattern.append(single_row_pattern[i] + single_row_pattern[j])

        triple_row_pattern = []
        for i in range(len(single_row_pattern)):
            for j in range(len(dual_row_pattern)):
                triple_row_pattern.append(single_row_pattern[i] + dual_row_pattern[j])

        for i in range(len(triple_row_pattern)):
            count_0 = triple_row_pattern[i].count(0)
            count_1 = triple_row_pattern[i].count(1)
            count_2 = triple_row_pattern[i].count(2)
            if (count_1 == variable_count[1]) and (count_0 == variable_count[0]) and count_2 == variable_count[2]:
                dictionary[str(list(triple_row_pattern[i]))] = list(triple_row_pattern[i])

    def merge_patterns(self, solved_dictionary, unsolved_dictionary):
        zero_error = 0
        intersection_error = 0
        x = 0
        for pattern_1 in unsolved_dictionary:
            percent = (x / len(unsolved_dictionary)) * 100
            stdout.write("\rProgress: %f " % percent)
            stdout.flush()
            array_1 = unsolved_dictionary[pattern_1]
            for pattern_2 in solved_dictionary:
                array_2 = solved_dictionary[pattern_2]

                # don't care about middle row
                array_2[5:10] = [0 if x == 0 else -1 for x in array_2[5:10]]

                # unsolved column replace with -1
                for i in range(len(array_2[:5])):
                    if (array_2[i] != 2) or (array_2[i + 10] != 2):
                        if array_2[i] != 0:
                            array_2[i] = -1

                        if array_2[i + 10] != 0:
                            array_2[i + 10] = -1

                # find collision between solved and unsolved
                ones = set([i for i, j in enumerate(array_1) if j == 1])
                twos = set([i for i, j in enumerate(array_2) if j >= 2])
                intersection = ones.intersection(twos)

                if len(intersection) > 0:
                    intersection_error += 1
                    continue

                # make sure zeros are at the same index
                zero_1 = [i for i, j in enumerate(array_1) if j == 0]
                zero_2 = [i for i, j in enumerate(array_2) if j == 0]

                if not(zero_1 == zero_2):
                    zero_error += 1
                    continue

                # merge arrays
                final_board = []
                for i in range(len(array_1)):
                    if array_2[i] >= 2:
                        final_board.append(array_2[i])
                    else:
                        final_board.append(array_1[i])

                self.pattern_dictionary[str(final_board)] = {
                    'array': final_board,
                    'steps': -1,
                    'moves': -1,
                    'final_mapping': -1
                }
            x += 1
        print('intersection error {}'.format(intersection_error))
        print('zero error {}'.format(zero_error))
        self.format_dictionary()

    def format_dictionary(self):
        for key in self.pattern_dictionary:
            array = self.pattern_dictionary[key]['array']
            pair = 2
            for i in range(5):
                if array[i] == 2:
                    array[i] = pair
                    array[i + 10] = pair
                    pair += 1
            self.pattern_dictionary[key]['array'] = array

    def save_patterns(self):
        print('{} patterns'.format(len(self.pattern_dictionary)))
        File.save_binary('pattern_dictionary.bin', self.pattern_dictionary)

    def create_mapping(self):
        pattern_dictionary = File.load_binary('pattern_dictionary.bin')
        for key in pattern_dictionary:
            initial_mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            array = pattern_dictionary[key]['array']
            current_position =  [i for i, j in enumerate(array) if j == 0]
            movements = pattern_dictionary[key]['moves']
            board = GameBoard(verbose=False)
            board.create_game_with_mapping(initial_mapping, current_position[0])
            for move in movements:
                if move == 'r':
                    board.move_right()
                elif move == 'l':
                    board.move_left()
                elif move == 'd':
                    board.move_down()
                elif move == 'u':
                    board.move_up()
            pattern_dictionary[key]['final_mapping'] = board.get_board_state()
        File.save_binary('pattern_dictionary.bin', pattern_dictionary)


if __name__ == '__main__':
    pd = PatternDatabase()
