from game_builder.board.game_board import GameBoard, GameDifficultyEnum
from random import randint
import numpy


class ReverseSolver:
    novice_goal_state = [1, 2, 2, 1, 1, 0, 3, 2, 3, 2, 1, 2, 2, 1, 1]
    apprentice_goal_state = [2, 1, 1, 2, 1, 0, 3, 3, 4, 4, 2, 1, 1, 2, 1]
    expert_goal_state = [2, 1, 4, 1, 5, 0, 3, 2, 2, 3, 2, 1, 4, 1, 5]
    master_goal_state = [1, 1, 5, 3, 4, 2, 2, 0, 6, 6, 1, 1, 5, 3, 4]

    int_to_move = {
        0: 'u',
        1: 'd',
        2: 'r',
        3: 'l'
    }

    reverse_int_to_move ={
        0: 'd',
        1: 'u',
        2: 'l',
        3: 'r'
    }

    def __init__(self, max_iter):
        self.board = GameBoard(verbose=False)
        self.max_iter = max_iter
        self.solutions = {}

    def set_difficulty(self, difficulty):
        if difficulty == GameDifficultyEnum.NOVICE:
            self.board.create_game_from_array(ReverseSolver.novice_goal_state)

    def solve(self, depth=0):
        if depth >= self.max_iter:
            return True

        game_state = self.board.get_board_state()
        if str(game_state) in self.solutions:
            return False

        self.solutions[str(game_state)] = ''

        depth += 1

        moves = numpy.array([0, 1, 2, 3])
        numpy.random.shuffle(moves)

        self.move(ReverseSolver.int_to_move[moves[0]])
        game_state = self.board.get_board_state()
        if self.solve(depth):
            self.solutions[str(game_state)] = [
                ReverseSolver.position_difference(game_state),
                ReverseSolver.incorrect_positions(game_state),
                ReverseSolver.reverse_int_to_move[moves[0]],
                depth
            ]
            return True
        self.undo_move(ReverseSolver.int_to_move[moves[0]])

        self.move(ReverseSolver.int_to_move[moves[1]])
        game_state = self.board.get_board_state()
        if self.solve(depth):
            self.solutions[str(game_state)] = [
                ReverseSolver.position_difference(game_state),
                ReverseSolver.incorrect_positions(game_state),
                ReverseSolver.reverse_int_to_move[moves[1]],
                depth
            ]
            return True
        self.undo_move(ReverseSolver.int_to_move[moves[1]])

        self.move(ReverseSolver.int_to_move[moves[2]])
        game_state = self.board.get_board_state()
        if self.solve(depth):
            self.solutions[str(game_state)] = [
                ReverseSolver.position_difference(game_state),
                ReverseSolver.incorrect_positions(game_state),
                ReverseSolver.reverse_int_to_move[moves[2]],
                depth
            ]
            return True
        self.undo_move(ReverseSolver.int_to_move[moves[2]])

        self.move(ReverseSolver.int_to_move[moves[3]])
        game_state = self.board.get_board_state()
        if self.solve(depth):
            self.solutions[str(game_state)] = [
                ReverseSolver.position_difference(game_state),
                ReverseSolver.incorrect_positions(game_state),
                ReverseSolver.reverse_int_to_move[moves[3]],
                depth
            ]
            return True
        self.undo_move(ReverseSolver.int_to_move[moves[3]])

    @staticmethod
    def incorrect_positions(game_state):
        return numpy.sum(numpy.array(game_state) != numpy.array(ReverseSolver.novice_goal_state))

    @staticmethod
    def position_difference(game_state):
        return numpy.subtract(numpy.array(game_state), numpy.array(ReverseSolver.novice_goal_state))

    def move(self, input_str):
        """
        move
        :param input_str: string
        :return: None
        """
        if input_str == 'u':
            self.board.move_up()
        elif input_str == 'd':
            self.board.move_down()
        elif input_str == 'l':
            self.board.move_left()
        elif input_str == 'r':
            self.board.move_right()

    def undo_move(self, input_str):
        """
        Undo a move
        :param input_str: string
        :return: None
        """
        if input_str == 'u':
            self.board.move_down()
        elif input_str == 'd':
            self.board.move_up()
        elif input_str == 'l':
            self.board.move_right()
        elif input_str == 'r':
            self.board.move_left()
