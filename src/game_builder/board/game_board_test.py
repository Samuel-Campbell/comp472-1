import unittest
from game_builder.board.game_board import GameBoard
import numpy


class TestGameBoard(unittest.TestCase):
    def test_top_row_solved(self):
        arr1 = numpy.array([
            0, 1, 1, 1, 1,
            2, 2, 3, 3, 4,
            6, 6, 5, 5, 4
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr1)
        self.assertFalse(board.top_row_solved()[0])
        arr2 = numpy.array([
            0, 1, 3, 3, 4,
            2, 2, 1, 1, 1,
            6, 6, 5, 5, 4
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr2)
        self.assertFalse(board.top_row_solved()[0])
        self.assertEqual(board.top_row_solved()[1], [0, 3])

        arr3 = numpy.array([
            0, 2, 3, 4, 1,
            6, 1, 5, 3, 1,
            6, 2, 5, 5, 4
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr3)
        self.assertFalse(board.top_row_solved()[0])
        self.assertEqual(board.top_row_solved()[1], [0])

        arr4 = numpy.array([
            6, 2, 3, 4, 1,
            0, 1, 5, 3, 1,
            6, 2, 5, 5, 4
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr4)
        self.assertTrue(board.top_row_solved()[0])
        self.assertEqual(board.top_row_solved()[1], [])

    def test_get_coordinates(self):
        arr = numpy.array([
            6, 2, 3, 4, 1,
            5, 1, 5, 3, 1,
            6, 2, 5, 0, 4
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        x, y = board.get_coordinates()
        self.assertEqual(x, 3)
        self.assertEqual(y, 2)

    def test_pattern_solved(self):
        arr = numpy.array([
            -1, -1, -1, -1, -1,
            1, 1, 0, -1, -1,
            -1, -1, -1, -1, -1
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        self.assertFalse(board.pattern_solved())

        arr = numpy.array([
            -1, -1, -1, 1, -1,
            -1, -1, 0, -1, -1,
            -1, -1, -1, 1, -1
        ])
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        self.assertTrue(board.pattern_solved())

        arr = [-1, -1, -1, -1, -1,
               1, 1, 0, -1, -1,
               -1, -1, -1, -1, -1]
        board = GameBoard(verbose=False)
        board.create_game_from_array(arr)
        self.assertFalse(board.pattern_solved())