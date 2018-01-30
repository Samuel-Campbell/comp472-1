from game_builder.board.game_board import GameBoard
from game_builder.game.auto_game import AutoGame


class TestModel:
    def __init__(self):
        pass

    @staticmethod
    def solve_puzzle(difficulty):
        """
        Use the AI to solve a pizzle given a certain difficulty

        :param difficulty: <int> [0-3] where 3 is the hardest
        :return: None
        """
        board = GameBoard()
        board.create_random_game(difficulty)
        game = AutoGame(board)
        game.run()