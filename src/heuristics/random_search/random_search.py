from random import randint
from game_builder.game.abstract_game import CommandEnum


class RandomSearch:
    def __init__(self, board, max_iter):
        self.board = board
        self.max_iter = max_iter
        self.permutations = {}

    def search(self, run):
        self.board.reset_board()
        iteration = 0
        moves = []
        while iteration < self.max_iter:
            state = self.board.get_board_state()
            move = self.__randomize_move()
            if move:
                moves.append([state, move])
                iteration += 1
            if self.board.game_cleared():
                moves.append([state, move])
                break
        if iteration < self.max_iter:
            self.permutations[run] = moves

    def __randomize_move(self):
        move = randint(0, 3)
        if move == 0:
            self.board.move_up()
        elif move == 1:
            self.board.move_down()
        elif move == 2:
            self.board.move_right()
        elif move == 3:
            self.board.move_left()
        return move

    def get_min(self):
        min_val = 9999
        key = None
        for searches in self.permutations:
            steps = (len(self.permutations[searches]))
            if steps < min_val:
                key = searches
                min_val = steps
        if key is not None:
            return self.permutations[key]

    def reset(self):
        self.permutations = {}
