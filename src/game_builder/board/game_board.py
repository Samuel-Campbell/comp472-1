import numpy
from game_builder.difficulty.game_difficulty import GameDifficultyEnum


class GameBoard:
    int_to_candy = {
        0: 'e',
        1: 'r',
        2: 'b',
        3: 'w',
        4: 'y',
        5: 'g',
        6: 'p'
    }

    candy_to_int = {
        'e': 0,
        'r': 1,
        'b': 2,
        'w': 3,
        'y': 4,
        'g': 5,
        'p': 6
    }

    position_to_letter = {
        (0, 0): 'A',
        (1, 0): 'B',
        (2, 0): 'C',
        (3, 0): 'D',
        (4, 0): 'E',
        (0, 1): 'F',
        (1, 1): 'G',
        (2, 1): 'H',
        (3, 1): 'I',
        (4, 1): 'J',
        (0, 2): 'K',
        (1, 2): 'L',
        (2, 2): 'M',
        (3, 2): 'N',
        (4, 2): 'O'
    }

    def __init__(self, verbose=True):
        self.__board = None
        self.__empty_cell = (0, 0)
        self.__verbose = verbose
        self.difficulty = None
        self.move_sequence = []

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
            self.__board[y][x + 1] = self.__board[y][x]
            self.__board[y][x] = tmp
            self.__empty_cell = (x + 1, y)
            move = self.position_to_letter[(x + 1, y)]
            self.move_sequence.append(move)
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
            self.__board[y + 1][x] = self.__board[y][x]
            self.__board[y][x] = tmp
            self.__empty_cell = (x, y + 1)
            move = self.position_to_letter[(x, y + 1)]
            self.move_sequence.append(move)
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
            self.__board[y][x - 1] = self.__board[y][x]
            self.__board[y][x] = tmp
            self.__empty_cell = (x - 1, y)
            move = self.position_to_letter[(x - 1, y)]
            self.move_sequence.append(move)
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
            self.__board[y - 1][x] = self.__board[y][x]
            self.__board[y][x] = tmp
            self.__empty_cell = (x, y - 1)
            move = self.position_to_letter[(x, y - 1)]
            self.move_sequence.append(move)
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
        self.difficulty = game_difficulty
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
        self.__find_empty_cell()

    @staticmethod
    def obtain_game_from_file(path):
        file = open(path, 'r')
        games_list = []
        for lines in file:
            lines = lines.replace('\n', '')
            line = lines.split(' ')
            line = [GameBoard.candy_to_int[x] for x in line]
            games_list.append(line)
        file.close()
        return games_list

    def create_game_with_mapping(self, array, value):
        top_row = array[:5]
        middle_row = array[5:10]
        bottom_row = array[-5:]
        self.__board = numpy.array([top_row, middle_row, bottom_row])
        self.__find_empty_cell(value)

    def create_game_from_array(self, array):
        top_row = array[:5]
        middle_row = array[5:10]
        bottom_row = array[-5:]
        self.__board = numpy.array([top_row, middle_row, bottom_row])
        self.__find_empty_cell()

    def copy(self):
        board = self.__board.copy()
        array = numpy.array(list(board[0]) + list(board[1]) + list(board[2]))
        board = GameBoard(verbose=False)
        board.create_game_from_array(array)
        return board

    def __find_empty_cell(self, value = 0):
        """
        Find where the empty cell is from the arrays.
        This is mandatory to know where the player is situated and whether a move is
        possible.

        :return: None
        """

        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                if self.__board[i, j] == value:
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
        print([self.int_to_candy[x] for x in self.__board[0]])
        print([self.int_to_candy[x] for x in self.__board[1]])
        print([self.int_to_candy[x] for x in self.__board[2]])

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

    def get_coordinates(self):
        return self.__empty_cell

    def pattern_solved(self):
        index0 = [i for i, j in enumerate(self.__board[0]) if j >= 1]
        index1 = [i for i, j in enumerate(self.__board[1]) if j >= 1]
        index2 = [i for i, j in enumerate(self.__board[2]) if j >= 1]
        content0 = [x for x in self.__board[0] if x > 0]
        content2 = [x for x in self.__board[2] if x > 0]
        if len(index0) == 0:
            return False
        elif len(index2) == 0:
            return False
        elif len(index1) > 0:
            return False
        return (index0 == index2) and (content0 == content2)

