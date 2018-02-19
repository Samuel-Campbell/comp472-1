import unittest

import numpy

from game_builder.board.game_board import GameBoard
from heuristics.strategic_solver.row_solver.bottom_row_solver import BottomRowSolver


class TestTopRowSolver(unittest.TestCase):
    def test_move_bottom_right(self):
        arr = numpy.array([
            1, 1, 1, 1, 1,
            0, 1, 1, 1, 1,
            1, 1, 1, 1, 6
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.move_bottom_right([0, 1], [4, 2], [0, 2])
        expected_result = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 6, 1, 1, 1, 1]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_move_middle_right(self):
        arr = numpy.array([
            1, 1, 1, 1, 1,
            0, 1, 1, 1, 6,
            1, 1, 1, 1, 1
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.move_middle_right([0, 1], [4, 1], [0, 2])
        expected_result = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 6, 1, 1, 1, 1]
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
        bs.move_corner_right()
        expected_result = numpy.array([2, 1, 1, 1, 1, 0, 5, 3, 3, 4, 2, 4, 5, 6, 6])
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_move_corner_bottom_right(self):
        arr = numpy.array([
            2, 1, 1, 1, 1,
            0, 2, 3, 3, 4,
            4, 5, 5, 6, 6
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.move_corner_bottom_right()
        expected_result = numpy.array([2, 1, 1, 1, 1, 0, 4, 3, 3, 4, 5, 2, 5, 6, 6])
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
        arr1 = numpy.array([
            1, 1, 1, 1, 1,
            1, 1, 1, 3, 0,
            4, 5, 6, 2, 1
        ])
        arr2 = numpy.array([
            1, 1, 1, 1, 1,
            1, 1, 3, 0, 1,
            4, 5, 6, 1, 1
        ])
        arr3 = numpy.array([
            1, 1, 1, 1, 1,
            1, 3, 0, 1, 1,
            4, 5, 1, 1, 1
        ])
        arr4 = numpy.array([
            1, 1, 1, 1, 1,
            3, 0, 1, 1, 1,
            4, 1, 1, 1, 1
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr1)
        bs = BottomRowSolver(board)
        bs.middle_left_1_square([4, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 4, 5, 6, 2, 3]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

        board = GameBoard(verbose=False)
        board.create_game_from_array(arr2)
        bs = BottomRowSolver(board)
        bs.middle_left_1_square([3, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 4, 5, 6, 3, 1]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

        board = GameBoard(verbose=False)
        board.create_game_from_array(arr3)
        bs = BottomRowSolver(board)
        bs.middle_left_1_square([2, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 4, 5, 3, 1, 1]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

        board = GameBoard(verbose=False)
        board.create_game_from_array(arr4)
        bs = BottomRowSolver(board)
        bs.middle_left_1_square([1, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 4, 3, 1, 1, 1]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_middle_left_2_square(self):
        arr1 = numpy.array([
            1, 1, 1, 1, 1,
            1, 1, 3, 1, 0,
            2, 6, 4, 5, 1
        ])
        arr2 = numpy.array([
            1, 1, 1, 1, 1,
            1, 3, 1, 0, 1,
            2, 6, 4, 1, 1
        ])
        arr3 = numpy.array([
            1, 1, 1, 1, 1,
            3, 1, 0, 1, 1,
            2, 4, 1, 1, 1
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr1)
        bs = BottomRowSolver(board)
        bs.middle_left_2_square([4, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 6, 4, 5, 3]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

        board = GameBoard(verbose=False)
        board.create_game_from_array(arr2)
        bs = BottomRowSolver(board)
        bs.middle_left_2_square([3, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 6, 4, 3, 1]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

        board = GameBoard(verbose=False)
        board.create_game_from_array(arr3)
        bs = BottomRowSolver(board)
        bs.middle_left_2_square([2, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 4, 3, 1, 1]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

    def test_middle_left_3_square(self):
        arr1 = numpy.array([
            1, 1, 1, 1, 1,
            3, 1, 1, 0, 1,
            2, 4, 5, 1, 1
        ])
        arr2 = numpy.array([
            1, 1, 1, 1, 1,
            1, 3, 1, 1, 0,
            2, 4, 5, 6, 1
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr1)
        bs = BottomRowSolver(board)
        bs.middle_left_3_square([3, 1])
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 4, 5, 3, 1]
        obtained_result = bs.board.get_board_state()
        for i in range(len(expected_result)):
            self.assertEqual(obtained_result[i], expected_result[i])

        board = GameBoard(verbose=False)
        board.create_game_from_array(arr2)
        bs = BottomRowSolver(board)
        bs.middle_left_3_square([4, 1])
        print(bs.board.get_board_state())
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 4, 5, 6, 3]
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

    def test_solve(self):
        arr = numpy.array([
            1, 2, 3, 4, 1,
            0, 1, 2, 6, 5,
            4, 5, 1, 6, 3
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        bs = BottomRowSolver(board)
        bs.solve()
        self.assertTrue(bs.board.game_cleared())
