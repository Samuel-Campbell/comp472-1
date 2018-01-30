from random import randint
from game_builder.game.abstract_game import CommandEnum


class RandomSearch:
    def __init__(self, board, max_iter):
        """
        Constructor

        :param board: <game_builder.board.game_board.GameBoard>
        :param max_iter: <int>
        """
        self.board = board
        self.board_sates = []
        self.max_iter = max_iter
        self.__best_permutation = []

    def search(self):
        """
        1) reset game board to original position
        2) while current iteration is less than max iteration --> keep playing
        3) make a random move
        4) if random move goes out of bounds then don't count it
        5) when game is cleared break from loop
        6) save permutation if game completed within max iterations

        :return: None
        """
        self.board.reset_board()
        iteration = 0
        moves = []
        while iteration < self.max_iter:
            state = self.board.get_board_state()
            next_move = self.__randomize_move()
            if next_move[0]:
                moves.append([state, next_move[1]])
                iteration += 1
            if self.board.game_cleared():
                break
        if iteration < self.max_iter:
            if len(self.__best_permutation) == 0:
                self.__best_permutation = moves.copy()
            elif len(self.__best_permutation) > len(moves):
                self.__best_permutation = moves.copy()

    def __randomize_move(self):
        """
        Randomize a move
        map ints [0, 3] to movements

        0: up
        1: down
        2: right
        3: left

        ** The boolean in the returned tuple is true if the move is valid
           and false if it was out of bounds.

        :return: boolean, <int> random move
        """
        move = randint(0, 3)
        result = False
        if move == 0:
            result = self.board.move_up()
        elif move == 1:
            result = self.board.move_down()
        elif move == 2:
            result = self.board.move_right()
        elif move == 3:
            result = self.board.move_left()
        return result, move

    def get_best_permutation(self):
        """
        returns the best permutation.
        The list must be parsed once to add the number of moves till the game ends.
        We do not know this value until the objective is reached so we must perform
        the calculations here

        :return: [np.array([]), int, int]
        """
        for i in range(len(self.__best_permutation)):
            self.__best_permutation[i] += [len(self.__best_permutation) - i]
        return self.__best_permutation
