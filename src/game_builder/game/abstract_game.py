import numpy


class CommandEnum:
    UP = 'u'
    RIGHT = 'r'
    DOWN = 'd'
    LEFT = 'l'
    MOVES = [UP, RIGHT, DOWN, LEFT]


class AbstractGame:
    def __init__(self, board):
        self._board = board

    def run(self):
        raise NotImplementedError

    def _move(self, input_str):
        raise NotImplementedError
