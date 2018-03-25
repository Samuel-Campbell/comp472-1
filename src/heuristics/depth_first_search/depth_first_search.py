import numpy
from game_builder.board.game_board import GameBoard
from util.file import File
from sys import stdout
from threading import Thread


class DepthFirstSearch:
    def __init__(self, board, max_iter=1):
        self.steps = 0
        self.move_sequence = []
        self.max_iter = max_iter
        self.board = board
        self.closed_states = {}

    def search(self, depth=0):
        if depth >= self.max_iter:
            return True

        game_state = self.board.get_board_state().copy()

        if str(game_state) in self.closed_states:
            return False

        self.closed_states[str(game_state)] = {
            'array': game_state,
            'moves'
        }

        depth += 1

        if self.board.move_right():
            if self.search(depth):
                self.move_sequence.append('l')
                return True
            self.board.move_left()

        if self.board.move_left():
            if self.search(depth):
                self.move_sequence.append('r')
                return True
            self.board.move_right()

        if self.board.move_up():
            if self.search(depth):
                self.move_sequence.append('d')
                return True
            self.board.move_down()

        if self.board.move_down():
            if self.search(depth):
                self.move_sequence.append('u')
                return True
            self.board.move_up()
        return False
