from util.file import File
from game_builder.board.game_board import GameBoard, GameDifficultyEnum
import itertools


class BestFirstSearch:
    pattern_dictionary = File.load_binary('pattern_dictionary.bin')

    def __init__(self, board):
        self.board = board

    def search(self):
        while not self.board.game_cleared():
            board_state = self.board.get_board_state()
            pairs = self.find_pairs(board_state)
            best_pattern = None
            move_count = 5000
            for pair in pairs:
                transformed_board = self.transform_board(board_state, pair)
                value = self.pattern_dictionary[str(transformed_board)]
                if value['steps'] < move_count:
                    move_count = value['steps']
                    best_pattern = value['moves']
            for move in best_pattern:
                if move == 'r':
                    self.board.move_right()
                elif move == 'l':
                    self.board.move_left()
                elif move == 'u':
                    self.board.move_up()
                else:
                    self.board.move_down()

    def find_pairs(self, array):
        pairs_array = [[], [], [], [], [], [], []]
        for i in range(len(array)):
            if i < 5:
                if array[i] == array[i + 10]:
                    pass
                else:
                    pairs_array[array[i]].append(i)
            elif i > 9:
                if array[i] == array[i - 10]:
                    pass
                else:
                    pairs_array[array[i]].append(i)
            else:
                pairs_array[array[i]].append(i)
        combinations = []
        for i in range(len(pairs_array)):
            combo = itertools.combinations(pairs_array[i], 2)
            for c in combo:
                combinations.append(c)
        return combinations

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


if __name__ == "__main__":
    moves = 0
    for i in range(50):
        board = GameBoard(verbose=False)
        board.create_random_game(GameDifficultyEnum.NOVICE)
        astar = BestFirstSearch(board)
        astar.search()
        moves += len(board.move_sequence)
