import unittest
from heuristics.strategic_solver.top_row_solver import TopRowSolver
from game_builder.board.game_board import GameBoard
import numpy
import time


class TestTopRowSolver(unittest.TestCase):
    def test_solve(self):
        arr = numpy.array([0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])
        start = time.time()
        for i in range(50):
            numpy.random.shuffle(arr)
            board = GameBoard(verbose=False)
            board.create_game_from_array(arr)
            ts = TopRowSolver(board)
            ts.solve()
            self.assertTrue(ts.board.top_row_solved()[0])
        end = time.time()
        diff = end - start
        self.assertLess(diff, 1)
