import numpy
from game_builder.difficulty.game_difficulty import GameDifficultyEnum


class GameBoard:
    int_to_candy = {
        0: ' ',
        1: 'r',
        2: 'b',
        3: 'w',
        4: 'y',
        5: 'g',
        6: 'p'
    }

    def __init__(self, verbose=True):
        self.__original_board = None
        self.__original_empty_cell = (0, 0)
        self.__board = None
        self.__empty_cell = (0, 0)
        self.__verbose = verbose

    def move_right(self):
        """
        Moves empty cell to the right
        Switches it's value in the array with the one on its right
        If the move is out of bounds then warn the user and do nothing.
        :return: boolean
        """

        x = self.__empty_cell[0]
        y = self.__empty_cell[1]
        if x < (len(self.__board[0]) - 1):
            tmp = self.__board[y][x + 1]
            self.__board[y][x + 1] = 0
            self.__board[y][x] = tmp
            self.__empty_cell = (x + 1, y)
            return True
        elif self.__verbose:
            print('Cannot move to cell.')
        return False

    def move_down(self):
        """
        Moves empty cell to the right
        :return: boolean
        """

        x = self.__empty_cell[0]
        y = self.__empty_cell[1]
        if y < (len(self.__board) - 1):
            tmp = self.__board[y + 1][x]
            self.__board[y + 1][x] = 0
            self.__board[y][x] = tmp
            self.__empty_cell = (x, y + 1)
            return True
        elif self.__verbose:
            print('Cannot move to cell.')
        return False
    
    def move_left(self):
        """
        Moves empty cell to the left
        Switches it's value in the array with the one on its left
        If the move is out of bounds then warn the user and do nothing.
        :return: boolean
        """

        x = self.__empty_cell[0]
        y = self.__empty_cell[1]
        if x > 0:
            tmp = self.__board[y][x - 1]
            self.__board[y][x - 1] = 0
            self.__board[y][x] = tmp
            self.__empty_cell = (x - 1, y)
            return True
        elif self.__verbose:
            print('Cannot move to cell.')
        return False
    
    def move_up(self):
        """
        Moves empty cell up
        :return: boolean
        """

        x = self.__empty_cell[0]
        y = self.__empty_cell[1]
        if y > 0:
            tmp = self.__board[y - 1][x]
            self.__board[y - 1][x] = 0
            self.__board[y][x] = tmp
            self.__empty_cell = (x, y - 1)
            return True
        elif self.__verbose:
            print('Cannot move to cell.')
        return False
    
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
            board_list = [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3]

        elif game_difficulty == GameDifficultyEnum.APPRENTICE:
            board_list = [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4]

        elif game_difficulty == GameDifficultyEnum.EXPERT:
            board_list = [0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5]

        elif game_difficulty == GameDifficultyEnum.MASTER:
            board_list = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
        board = numpy.array(board_list)
        numpy.random.shuffle(board)
        top_row = board[:5]
        middle_row = board[5:10]
        bottom_row = board[-5:]
        self.__board = numpy.array([top_row, middle_row, bottom_row])
        self.__original_board = self.__board.copy()
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
                if self.__board[i, j] == 0:
                    self.__empty_cell = (j, i)
                    self.__original_empty_cell = (j, i)

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

    def get_board_state(self):
        """
        :return: copy of the board
        """
        board = self.__board.copy()
        return numpy.array(list(board[0]) + list(board[1]) + list(board[2]))

    def reset_board(self):
        """
        resets board to original state
        :return: None
        """
        self.__board = self.__original_board.copy()
        self.__empty_cell = self.__original_empty_cell[0], self.__original_empty_cell[1]
