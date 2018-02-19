from game_builder.game.abstract_game import CommandEnum
import time


class AbstractRowSolver:
    def __init__(self, board, verbose=False, output=False):
        self.board = board
        self.verbose = verbose
        self.nb_moves = 0
        self.move = []

    def solve(self):
        raise NotImplementedError

    def _go_left_center(self):
        x, y = self.board.get_coordinates()
        for i in range(x):
            self._move(CommandEnum.LEFT)
        if y == 2:
            self._move(CommandEnum.UP)
        elif y == 0:
            self._move(CommandEnum.DOWN)

    def _move(self, input_str):
        """
        move
        :param input_str: string
        :return: None
        """
        if input_str == CommandEnum.UP:
            self.board.move_up()
        elif input_str == CommandEnum.DOWN:
            self.board.move_down()
        elif input_str == CommandEnum.LEFT:
            self.board.move_left()
        elif input_str == CommandEnum.RIGHT:
            self.board.move_right()
        self.nb_moves += 1
        if self.verbose:
            self.board.display()
            time.sleep(0.2)