import numpy
from game_builder.board.game_board import GameBoard
from util.file import File
from sys import stdout


class DepthFirstSearch:
    def __init__(self, board, max_iter=1):
        self.steps = 0
        self.move_sequence = []
        self.max_iter = max_iter
        self.board = board
        self.closed_states = {}

    def search(self, depth=0):
        if depth >= self.max_iter:
            return False

        if self.board.pattern_solved():
            self.steps = depth
            return True

        game_state = self.board.get_board_state()

        if str(game_state) in self.closed_states:
            return False

        self.closed_states[str(game_state)] = 1
        depth += 1

        if self.board.move_right():
            if self.search(depth):
                self.move_sequence.append('r')
                return True
            self.board.move_left()

        if self.board.move_left():
            if self.search(depth):
                self.move_sequence.append('l')
                return True
            self.board.move_right()

        if self.board.move_up():
            if self.search(depth):
                self.move_sequence.append('u')
                return True
            self.board.move_down()

        if self.board.move_down():
            if self.search(depth):
                self.move_sequence.append('d')
                return True
            self.board.move_up()

        return False


if __name__ == '__main__':
    pattern_dictionary = File.load_binary('pattern_dictionary.bin')
    i = 0
    for key in pattern_dictionary:
        percent = i / len(pattern_dictionary) * 100
        max_iter = 35
        i += 1
        if pattern_dictionary[key]['steps'] == -1:
            while True:
                stdout.write("\rProgress: {} Iteration: {}".format(percent, max_iter))
                stdout.flush()
                board = GameBoard(verbose=False)
                board.create_game_from_array(pattern_dictionary[key]['array'])
                dfs = DepthFirstSearch(board, max_iter)
                result = dfs.search()
                if result:
                    pattern_dictionary[key]['steps'] = dfs.steps
                    dfs.move_sequence.reverse()
                    pattern_dictionary[key]['moves'] = dfs.move_sequence
                    File.save_binary('pattern_dictionary.bin', pattern_dictionary)
                    break
                max_iter += 1
    print()
    File.save_binary('pattern_dictionary.bin', pattern_dictionary)