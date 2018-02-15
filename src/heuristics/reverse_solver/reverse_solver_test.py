import unittest

from game_builder.board.game_board import GameBoard
from heuristics.reverse_solver.reverse_solver import ReverseSolver


class TestReverseSolver(unittest.TestCase):
    def test_goal_states(self):
        board = GameBoard()
        board.create_game_from_array(ReverseSolver.novice_goal_state)
        self.assertTrue(board.game_cleared())

        board.create_game_from_array(ReverseSolver.apprentice_goal_state)
        self.assertTrue(board.game_cleared())

        board.create_game_from_array(ReverseSolver.expert_goal_state)
        self.assertTrue(board.game_cleared())

        board.create_game_from_array(ReverseSolver.master_goal_state)
        self.assertTrue(board.game_cleared())

        rs = ReverseSolver(22)
        org = [1, 2, 2, 1, 1, 0, 3, 2, 3, 2, 1, 2, 2, 1, 1]
        arr = [3, 1, 2, 1, 1, 0, 2, 2, 2, 3, 1, 2, 2, 1, 1]
        print(rs.position_difference(arr))