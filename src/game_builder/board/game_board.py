import numpy
from game_builder.difficulty.game_difficulty import GameDifficultyEnum


class GameBoard:
    board = None
    empty_cell = (0, 0)

    def __init__(self):
        pass

    @staticmethod
    def move_right():
        x = GameBoard.empty_cell[0]
        y = GameBoard.empty_cell[1]
        if x < (len(GameBoard.board[0]) - 1):
            tmp = GameBoard.board[y][x + 1]
            GameBoard.board[y][x + 1] = ' '
            GameBoard.board[y][x] = tmp
            GameBoard.empty_cell = (x + 1, y)
        else:
            print('Cannot move to cell.')

    @staticmethod
    def move_down():
        x = GameBoard.empty_cell[0]
        y = GameBoard.empty_cell[1]
        if y < (len(GameBoard.board) - 1):
            tmp = GameBoard.board[y + 1][x]
            GameBoard.board[y + 1][x] = ' '
            GameBoard.board[y][x] = tmp
            GameBoard.empty_cell = (x, y + 1)
        else:
            print('Cannot move to cell.')

    @staticmethod
    def move_left():
        x = GameBoard.empty_cell[0]
        y = GameBoard.empty_cell[1]
        if x > 0:
            tmp = GameBoard.board[y][x - 1]
            GameBoard.board[y][x - 1] = ' '
            GameBoard.board[y][x] = tmp
            GameBoard.empty_cell = (x - 1, y)
        else:
            print('Cannot move to cell.')

    @staticmethod
    def move_up():
        x = GameBoard.empty_cell[0]
        y = GameBoard.empty_cell[1]
        if y > 0:
            tmp = GameBoard.board[y - 1][x]
            GameBoard.board[y - 1][x] = ' '
            GameBoard.board[y][x] = tmp
            GameBoard.empty_cell = (x, y - 1)
        else:
            print('Cannot move to cell.')

    @staticmethod
    def create_random_game(game_difficulty):
        board_list = []
        if game_difficulty == GameDifficultyEnum.NOVICE:
            board_list = [' ', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'w', 'w']

        elif game_difficulty == GameDifficultyEnum.APPRENTICE:
            board_list = [' ', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'w', 'w', 'y', 'y']

        elif game_difficulty == GameDifficultyEnum.EXPERT:
            board_list = [' ', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'w', 'w', 'y', 'y', 'g', 'g']

        elif game_difficulty == GameDifficultyEnum.MASTER:
            board_list = [' ', 'r', 'r', 'r', 'r', 'b', 'b', 'w', 'w', 'y', 'y', 'g', 'g', 'p', 'p']
        board = numpy.array(board_list)
        numpy.random.shuffle(board)
        top_row = board[:5]
        middle_row = board[5:10]
        bottom_row = board[-5:]
        GameBoard.board = numpy.array([top_row, middle_row, bottom_row])
        GameBoard.__find_empty_cell()
        return GameBoard.board

    @staticmethod
    def create_game_from_file():
        pass

    @staticmethod
    def __find_empty_cell():
        for i in range(len(GameBoard.board)):
            for j in range(len(GameBoard.board[i])):
                if GameBoard.board[i, j] == ' ':
                    GameBoard.empty_cell = (j, i)
