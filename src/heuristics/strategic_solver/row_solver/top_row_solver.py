from game_builder.game.abstract_game import CommandEnum
from heuristics.strategic_solver.row_solver.abstract_row_solver import AbstractRowSolver


class TopAlgorithm:
    """
    x F x x x       x I F x x
    x   I x x  ==>  x   x x x
    x x x x x       x x x x x

    """
    right_to_top = [
        CommandEnum.RIGHT,
        CommandEnum.UP,
        CommandEnum.LEFT,
        CommandEnum.DOWN
    ]

    """    
    x F x x x       x I F x x
    x   x x x  ==>  x   x x x
    x I x x x       x x x x x

    """
    bottom_to_top_has_right = [
        CommandEnum.DOWN,
        CommandEnum.RIGHT,
        CommandEnum.UP,
        CommandEnum.UP,
        CommandEnum.LEFT,
        CommandEnum.DOWN
    ]

    """    
    x x x S F       x x x I S
    x   x x x  ==>  x   x F x
    x x x x I       x x x x x

    """
    bottom_to_top_has_left = [
        CommandEnum.DOWN,
        CommandEnum.LEFT,
        CommandEnum.UP,
        CommandEnum.RIGHT,
        CommandEnum.UP,
        CommandEnum.LEFT,
        CommandEnum.DOWN
    ]

    """
    x x x S F       x x x I S
    x x x I    ==>  x x x F  
    x x x x x       x x x x x

    """
    left_to_top = [
        CommandEnum.UP,
        CommandEnum.LEFT,
        CommandEnum.DOWN
    ]

    def __init__(self):
        pass


class TopRowSolver(AbstractRowSolver):
    def __init__(self, board, verbose=False, output=False):
        AbstractRowSolver.__init__(self, board, verbose, output)

    def solve(self):
        solved, resolve = self.board.top_row_solved()
        if solved:
            return
        self._go_left_center()
        direction = 'r'
        i = 0
        while True:
            solved, resolve = self.board.top_row_solved()
            if solved:
                break
            game_state = self.board.get_board_state()
            if game_state[i] in resolve:
                down = game_state[i + 10]
                if i == 0:
                    left = None
                    right = game_state[i + 6]
                if i == 4:
                    left = game_state[i + 4]
                    right = None
                else:
                    left = game_state[i + 4]
                    right = game_state[i + 6]
                self.__find_and_replace(down, left, right, resolve)
            if i == 4:
                direction = 'l'
            elif i == 0:
                direction = 'r'

            if direction == 'r':
                i += 1
                self._move(CommandEnum.RIGHT)
            else:
                i -= 1
                self._move(CommandEnum.LEFT)

    def __find_and_replace(self, down, left, right, ignore):
        algorithm = []
        if (right is not None) and (right not in ignore):
            algorithm = TopAlgorithm.right_to_top
        elif (right is not None) and (down not in ignore):
            algorithm = TopAlgorithm.bottom_to_top_has_right
        elif (left is not None) and (left not in ignore):
            algorithm = TopAlgorithm.left_to_top
        elif (left is not None) and (down not in ignore):
            algorithm = TopAlgorithm.bottom_to_top_has_left
        for move in algorithm:
            self._move(move)

