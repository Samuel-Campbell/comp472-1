import numpy
from game_builder.difficulty.game_difficulty import GameDifficultyEnum


class GameBoard:
    board = None

    def __init__(self):
        pass

    @staticmethod
    def create_random_game(game_difficulty):
        board_list = []
        if game_difficulty == GameDifficultyEnum.NOVICE:
            board_list = ['', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'w', 'w']

        elif game_difficulty == GameDifficultyEnum.APPRENTICE:
            board_list = ['', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'w', 'w', 'y', 'y']

        elif game_difficulty == GameDifficultyEnum.EXPERT:
            board_list = ['', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'w', 'w', 'y', 'y', 'g', 'g']

        elif game_difficulty == GameDifficultyEnum.MASTER:
            board_list = ['', 'r', 'r', 'r', 'r', 'b', 'b', 'w', 'w', 'y', 'y', 'g', 'g', 'p', 'p']
        GameBoard.board = numpy.array(board_list)
        numpy.random.shuffle(GameBoard.board)
        return GameBoard.board

    @staticmethod
    def create_game_from_file():
        pass