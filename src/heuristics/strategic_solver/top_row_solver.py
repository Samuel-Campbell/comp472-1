from game_builder.game.abstract_game import CommandEnum


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


class TopRowSolver:
    def __init__(self, board):
        self.board = board
        self.state = {}

    def solve(self):
        self.__go_left_center()
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
                self.__move(CommandEnum.RIGHT)
            else:
                i -= 1
                self.__move(CommandEnum.LEFT)

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
            self.__move(move)

    def __go_left_center(self):
        x, y = self.board.get_coordinates()
        for i in range(x):
            self.__move(CommandEnum.LEFT)
        if y == 2:
            self.__move(CommandEnum.UP)
        elif y == 0:
            self.__move(CommandEnum.DOWN)

    def __move(self, input_str):
        """
        move
        :param input_str: string
        :return: None
        """
        if input_str == CommandEnum.UP:
            self.board.move_up()
        elif input_str == CommandEnum.DOWN:
            self.board.move_down()
        elif input_str == CommandEnum.LEFT:
            self.board.move_left()
        elif input_str == CommandEnum.RIGHT:
            self.board.move_right()
