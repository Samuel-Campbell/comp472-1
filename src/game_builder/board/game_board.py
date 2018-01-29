import numpy
from game_builder.difficulty.game_difficulty import GameDifficultyEnum


class GameBoard:
    def __init__(self):
        self.__board = None
        self.__empty_cell = (0, 0)

    def move_right(self):
        """
        Moves empty cell to the right
        Switches it's value in the array with the one on its right
        If the move is out of bounds then warn the user and do nothing.
        :return: None
        """

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
        """
        Moves empty cell to the right
        :return: None
        """

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
        """
        Moves empty cell to the left
        Switches it's value in the array with the one on its left
        If the move is out of bounds then warn the user and do nothing.
        :return: None
        """

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
        """
        Moves empty cell up
        :return: None
        """

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
        """
        Creates a random board based on the game difficulty
        The board has the dimensions 5 X 3
        top row: [x, x, x, x, x]
        mid row: [x, x, x, x, x]
        bot row: [x, x, x, x, x]

        The higher the difficulty the more different characters appear in the arrays

        :param game_difficulty: GameDifficultyEnum --> '0', '1', '2', '3'
        :return: None
        """

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
        raise NotImplementedError
    
    def __find_empty_cell(self):
        """
        Find where the empty cell is from the arrays.
        This is mandatory to know where the player is situated and whether a move is
        possible.

        :return: None
        """
        
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                if self.__board[i, j] == ' ':
                    self.__empty_cell = (j, i)

    def display(self):
        """
        Displays the board on the command line
        __board[0] --> top row
        __board[1] --> middle row
        __board[2] --> bottom row

        :return: None
        """

        print()
        print(self.__board[0])
        print(self.__board[1])
        print(self.__board[2])

    def game_cleared(self):
        """
        Returns true if the top row and bottom row are the same
        else it returns False

        :return: boolean
        """

        if numpy.array_equal(self.__board[0], self.__board[2]):
            return True
        return False
