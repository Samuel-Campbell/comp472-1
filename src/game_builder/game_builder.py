from game_builder.mode.game_mode import GameMode, PlayModeEnum
from game_builder.difficulty.game_difficulty import GameDifficulty
from game_builder.board.game_board import GameBoard
from game_builder.game.manual_game import ManualGame
from game_builder.game.auto_game import AutoGame


class GameBuilder:
    def __init__(self):
        pass

    @staticmethod
    def build():
        mode = GameMode.run()
        difficulty = GameDifficulty.run()
        if mode == PlayModeEnum.MANUAL:
            board = GameBoard()
            board.create_random_game(difficulty)
            return ManualGame(board)
        else:
            # Use multi threading in the future here.
            # 1 per processor so that ML can solve multiple boards
            board = GameBoard()
            board = board.create_game_from_file(None)
            return AutoGame(board)
