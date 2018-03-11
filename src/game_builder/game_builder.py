from game_builder.mode.game_mode import GameMode, PlayModeEnum
from game_builder.difficulty.game_difficulty import GameDifficulty
from game_builder.board.game_board import GameBoard
from game_builder.game.manual_game import ManualGame
from game_builder.game.auto_game import AutoGame
import os


class GameBuilder:
    def __init__(self):
        pass

    @staticmethod
    def build():
        """
        Builder pattern
        1) Ask user for game mode
        2) Ask user for game difficulty
        3) If mode set to manual then create a random board
        4) if mode set to auto then use ML model to solve puzzle
        :return: None
        """

        mode = GameMode.run()

        root_directory = os.path.abspath(__file__ + "r/../../")
        rel_path = r'data/game/'
        directory_path = os.path.join(root_directory, rel_path)
        games = []

        for filename in os.listdir(directory_path):
            games += GameBoard.obtain_game_from_file(directory_path + filename)

        if mode == PlayModeEnum.MANUAL:
            for game in games:
                board = GameBoard()
                board.create_game_from_array(game)
                print('------------------------------------------------')
                game = ManualGame(board)
                game.run()
        else:
            for game in games:
                board = GameBoard(verbose=False)
                board.create_game_from_array(game)
                game = AutoGame(board)
                game.run()

        print('Solved {} games.'.format(len(games)))
