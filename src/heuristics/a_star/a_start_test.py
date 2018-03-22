import unittest
from heuristics.a_star.a_star import AStar
from game_builder.board.game_board import GameBoard, GameDifficultyEnum


class TestAStar(unittest.TestCase):
    def test_find_pairs(self):
        astar = AStar(None)
        array = [0, 1, 2, 3, 4,
                 5, 6, 1, 2, 3,
                 4, 1, 6, 1, 4]
        result = astar.find_pairs(array)
        expected_result = [(1, 7), (1, 13), (7, 11), (7, 13), (11, 13), (2, 8), (3, 9), (4, 10), (10, 14), (6, 12)]
        print(result)
        #self.assertEqual(expected_result, result)

    def test_transform_bord(self):
        astar = AStar(None)
        array = \
            [0, 1, 2, 3, 4,
             5, 6, 1, 2, 3,
             4, 1, 6, 1, 4]
        result = astar.transform_board(array, (7, 13))
        expected_result = [0, 2, -1, -1, 2, -1, -1, 1, -1, -1, -1, 2, -1, 1, 2]
        self.assertEqual(result, expected_result)

    def test_search(self):
        board = GameBoard(verbose=False)
        board.create_random_game(GameDifficultyEnum.MASTER)
        astar = AStar(board)
        astar.search()
