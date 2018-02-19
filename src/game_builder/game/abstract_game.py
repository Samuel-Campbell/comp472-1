import numpy


class CommandEnum:
    UP = 'w'
    RIGHT = 's'
    DOWN = 's'
    LEFT = 'a'
    MOVES = [UP, RIGHT, DOWN, LEFT]


class AbstractGame:
    def __init__(self, board):
        self._board = board

    def run(self):
        raise NotImplementedError

    def _move(self, input_str):
        """
        Moves the empty cell up, left, down, or right based on input_str
        UP: 'w'
        DOWN: 's'
        LEFT: 'a'
        RIGHT: 'd'

        :param input_str: string
        :return: None
        """

        if input_str == CommandEnum.LEFT:
            self._board.move_left()

        elif input_str == CommandEnum.RIGHT:
            self._board.move_right()

        elif input_str == CommandEnum.UP:
            self._board.move_up()

        elif input_str == CommandEnum.DOWN:
            self._board.move_down()