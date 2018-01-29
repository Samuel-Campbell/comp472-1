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
            board = GameBoard.create_random_game(difficulty)
            return ManualGame(board)
        else:
            board = GameBoard.create_game_from_file()
            return AutoGame(board)
