import numpy
from game_builder.difficulty.game_difficulty import GameDifficultyEnum


class GameBoard:
    def __init__(self):
        self.__board = None
        self.__empty_cell = (0, 0)

    def move_right(self):
        x = self.__empty_cell[0]
        y = self.__empty_cell[1]
        if x < (len(self.__board[0]) - 1):
            tmp = self.__board[y][x + 1]
            self.__board[y][x + 1] = ' '
            self.__board[y][x] = tmp
            self.__empty_cell = (x + 1, y)
        else:
            print('Cannot move to cell.')

    def move_down(self):
        x = self.__empty_cell[0]
        y = self.__empty_cell[1]
        if y < (len(self.__board) - 1):
            tmp = self.__board[y + 1][x]
            self.__board[y + 1][x] = ' '
            self.__board[y][x] = tmp
            self.__empty_cell = (x, y + 1)
        else:
            print('Cannot move to cell.')
    
    def move_left(self):
        x = self.__empty_cell[0]
        y = self.__empty_cell[1]
        if x > 0:
            tmp = self.__board[y][x - 1]
            self.__board[y][x - 1] = ' '
            self.__board[y][x] = tmp
            self.__empty_cell = (x - 1, y)
        else:
            print('Cannot move to cell.')
    
    def move_up(self):
        x = self.__empty_cell[0]
        y = self.__empty_cell[1]
        if y > 0:
            tmp = self.__board[y - 1][x]
            self.__board[y - 1][x] = ' '
            self.__board[y][x] = tmp
            self.__empty_cell = (x, y - 1)
        else:
            print('Cannot move to cell.')
    
    def create_random_game(self, game_difficulty):
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
        self.__board = numpy.array([top_row, middle_row, bottom_row])
        self.__find_empty_cell()
    
    def create_game_from_file(self, path):
        pass
    
    def __find_empty_cell(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                if self.__board[i, j] == ' ':
                    self.__empty_cell = (j, i)

    def display(self):
        print()
        print(self.__board[0])
        print(self.__board[1])
        print(self.__board[2])

    def game_cleared(self):
        if numpy.array_equal(self.__board[0], self.__board[2]):
            return True
        return False
