from random import randint
from game_builder.game.abstract_game import CommandEnum


class RandomSearch:
    def __init__(self, board, max_iter):
        self.board = board
        self.board_sates = []
        self.max_iter = max_iter
        self.__best_permutation = []

    def search(self, run):
        self.board.reset_board()
        iteration = 0
        moves = []
        while iteration < self.max_iter:
            state = self.board.get_board_state()
            next_move = self.__randomize_move()
            if next_move[0]:
                moves.append([state, next_move[1]])
                iteration += 1
            if self.board.game_cleared():
                break
        if iteration < self.max_iter:
            if len(self.__best_permutation) == 0:
                self.__best_permutation = moves.copy()
            elif len(self.__best_permutation) > len(moves):
                self.__best_permutation = moves.copy()

    def __randomize_move(self):
        move = randint(0, 3)
        result = False
        if move == 0:
            result = self.board.move_up()
        elif move == 1:
            result = self.board.move_down()
        elif move == 2:
            result = self.board.move_right()
        elif move == 3:
            result = self.board.move_left()
        return result, move

    def get_best_permutation(self):
        for i in range(len(self.__best_permutation)):
            self.__best_permutation[i] += [len(self.__best_permutation) - i]
        return self.__best_permutation
