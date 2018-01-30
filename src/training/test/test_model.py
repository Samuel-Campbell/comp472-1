from game_builder.board.game_board import GameBoard
from game_builder.game.auto_game import AutoGame


class TestModel:
    def __init__(self):
        pass

    @staticmethod
    def solve_puzzle(difficulty):
        board = GameBoard()
        board.create_random_game(difficulty)
        game = AutoGame(board)
        game.run()