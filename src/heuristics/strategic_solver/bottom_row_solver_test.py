import unittest
from heuristics.strategic_solver.bottom_row_solver import BottomRowSolver
from game_builder.board.game_board import GameBoard
import numpy
import time


class TestTopRowSolver(unittest.TestCase):
    def test_move_bottom_right(self):
        arr = numpy.array([
            2, 1, 1, 1, 1,
            0, 2, 3, 3, 4,
            4, 5, 5, 6, 6
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.solve()
        bs.move_bottom_right([0, 1], [4, 2])
        expected_result = numpy.array([2, 1, 1, 1, 1, 2, 3, 3, 0, 6, 4, 5, 5, 4, 6])
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_move_middle_right(self):
        arr = numpy.array([
            2, 1, 1, 1, 1,
            0, 2, 3, 3, 4,
            4, 5, 5, 6, 6
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.solve()
        bs.move_middle_right([0, 1], [4, 1], [0, 2])
        expected_result = numpy.array([2, 1, 1, 1, 1, 0, 4, 3, 5, 6, 3, 2, 4, 5, 6])
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_move_corner_right(self):
        arr = numpy.array([
            2, 1, 1, 1, 1,
            0, 2, 3, 3, 4,
            4, 5, 5, 6, 6
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.solve()
        bs.move_corner_right()
        expected_result = numpy.array([2, 1, 1, 1, 1, 5, 0, 3, 3, 4, 2, 4, 5, 6, 6])
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_cycle_counter_clockwise(self):
        arr = numpy.array([
            2, 1, 1, 1, 1,
            4, 2, 3, 3, 0,
            4, 5, 5, 6, 6
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.cycle_counter_clockwise([4, 1])
        expected_result = [2, 1, 1, 1, 1, 4, 4, 2, 3, 0, 5, 5, 6, 6, 3]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_cycle_clockwise(self):
        arr = numpy.array([
            2, 1, 1, 1, 1,
            4, 2, 3, 3, 0,
            4, 5, 5, 6, 6
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.cycle_clockwise([4, 1])
        expected_result = [2, 1, 1, 1, 1, 2, 3, 3, 6, 0, 4, 4, 5, 5, 6]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_middle_left_1_square(self):
        arr = numpy.array([
            2, 1, 1, 1, 1,
            4, 2, 1, 3, 0,
            4, 5, 5, 6, 4
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.middle_left_1_square([4, 1])
        expected_result = [2, 1, 1, 1, 1, 4, 2, 4, 1, 0, 4, 5, 5, 6, 3]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_middle_left_2_square(self):
        arr = numpy.array([
            1, 1, 1, 1, 1,
            1, 1, 3, 1, 0,
            2, 2, 2, 2, 1
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.middle_left_2_square([4, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 3]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_middle_left_3_square(self):
        arr = numpy.array([
            1, 1, 1, 1, 1,
            1, 3, 1, 1, 0,
            2, 2, 2, 2, 1
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.middle_left_3_square([4, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 3]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_middle_left_4_square(self):
        arr = numpy.array([
            1, 1, 1, 1, 1,
            3, 1, 1, 1, 0,
            2, 2, 2, 2, 1
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.middle_left_4_square([4, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 3]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])