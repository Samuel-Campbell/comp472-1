from training.classifier.abstract_classifier import AbstractClassifier
import time


class DepthFirstSearch:
    clf = AbstractClassifier(None)

    move_to_int = {
        'u': 0,
        'd': 1,
        'r': 2,
        'l': 3
    }

    def __init__(self, board, max_iter=1000):
        self.board = board
        self.max_iter = max_iter
        self.permutation = []
        self.full_depth = 0

    def search(self, depth=0):
        if depth >= self.max_iter:
            return False
        if self.board.game_cleared():
            self.full_depth = depth
            return True

        depth += 1
        probabilities = DepthFirstSearch.clf.predict_probabilities(self.board.get_board_state())
        probabilities.sort(key=lambda x: x[0])
        first_best = probabilities.pop()[1]
        second_best = probabilities.pop()[1]
        third_best = probabilities.pop()[1]
        fourth_best = probabilities.pop()[1]
        game_state = self.board.get_board_state().copy()

        self.move(first_best)
        if self.search(depth):
            self.permutation.append(
                [game_state, self.move_to_int[first_best], self.full_depth - depth + 1])
            return True
        self.undo_move(first_best)

        self.move(second_best)
        if self.search(depth):
            self.permutation.append(
                [game_state, self.move_to_int[second_best], self.full_depth - depth + 1])
            return True
        self.undo_move(second_best)

        self.move(third_best)
        if self.search(depth):
            self.permutation.append(
                [game_state, self.move_to_int[third_best], self.full_depth - depth + 1])
            return True
        self.undo_move(third_best)

        self.move(fourth_best)
        if self.search(depth):
            self.permutation.append(
                [game_state, self.move_to_int[fourth_best], self.full_depth - depth + 1])
            return True
        self.undo_move(fourth_best)

        return False

    def move(self, input_str):
        if input_str == 'u':
            self.board.move_up()
        elif input_str == 'd':
            self.board.move_down()
        elif input_str == 'l':
            self.board.move_left()
        elif input_str == 'r':
            self.board.move_right()

    def undo_move(self, input_str):
        if input_str == 'u':
            self.board.move_down()
        elif input_str == 'd':
            self.board.move_up()
        elif input_str == 'l':
            self.board.move_right()
        elif input_str == 'r':
            self.board.move_left()