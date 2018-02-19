import unittest
from heuristics.strategic_solver.strategic_solver import StrategicSolver
from game_builder.board.game_board import GameBoard
import numpy
import time


class TestStrategicSolver(unittest.TestCase):
    def test_solve(self):
        arr = numpy.array([0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])
        start = time.time()
        for i in range(50):
            numpy.random.shuffle(arr)
            board = GameBoard(verbose=False)
            board.create_game_from_array(arr)
            ss = StrategicSolver(board)
            ss.solve()
            self.assertTrue(ss.board.game_cleared())
        end = time.time()
        print(end - start)