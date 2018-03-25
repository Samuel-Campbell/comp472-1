from itertools import permutations
from util.file import File
from sys import stdout
from game_builder.board.game_board import GameBoard


class PatternDatabase:
    def __init__(self):
        self.pattern_dictionary = {}

    def find_patterns(self):
        middle_row_pattern = list(set(permutations([0, -1, -1, -1,- 1], 5)))
        for i in range(len(middle_row_pattern)):
            key = str([2, 2, 2, 2, 2] + list(middle_row_pattern[i]) + [2, 2, 2, 2, 2])
            self.pattern_dictionary[key] = {
                'steps': 0,
                'array': [2, 3, 4, 5, 6] + list(middle_row_pattern[i]) + [2, 3, 4, 5, 6]
            }

    def reverse_solver(self):
        end_states = []
        for key in self.pattern_dictionary:
            end_states.append(self.pattern_dictionary[key]['array'])

        for array in end_states:
            board = GameBoard(verbose=False)
            board.create_game_from_array(array)

    def depth_first_search(selfa):

    def transform_board(self, array, pair):
        transformed_array = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        zero_index = [i for i, j in enumerate(array) if j == 0][0]
        for i in range(5):
            if array[i] == array[i + 10]:
                transformed_array[i] = 2
                transformed_array[i + 10] = 2
        transformed_array[pair[0]] = 1
        transformed_array[pair[1]] = 1
        transformed_array[zero_index] = 0
        return transformed_array


if __name__ == '__main__':
    pd = PatternDatabase()
    pd.find_patterns()




