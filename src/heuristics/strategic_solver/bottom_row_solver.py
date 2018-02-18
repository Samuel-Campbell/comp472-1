from game_builder.game.abstract_game import CommandEnum
from game_builder.board.game_board import GameBoard


class BottomAlgorithm:
    bottom_right = [
        CommandEnum.RIGHT, #variable till
        CommandEnum.DOWN,
        CommandEnum.LEFT,
        CommandEnum.UP
    ]

    middle_right = [
        CommandEnum.RIGHT,  # variable
        # loop till corner_right
        CommandEnum.DOWN,
        CommandEnum.LEFT,
        CommandEnum.LEFT,
        CommandEnum.LEFT,
        CommandEnum.UP,
        CommandEnum.RIGHT,
        CommandEnum.RIGHT,
        # loop
        CommandEnum.DOWN,
        CommandEnum.LEFT,
        CommandEnum.LEFT,
        CommandEnum.UP
    ]

    corner_right = [
        CommandEnum.DOWN,
        CommandEnum.RIGHT,
        CommandEnum.UP,
        CommandEnum.LEFT,
        CommandEnum.DOWN,
        CommandEnum.RIGHT,
        CommandEnum.UP
    ]

    cycle_counter_clockwise = [
        CommandEnum.LEFT,
        CommandEnum.DOWN,
        CommandEnum.RIGHT,
        CommandEnum.UP,
        CommandEnum.LEFT
    ]

    cycle_clockwise = [
        CommandEnum.RIGHT,
        CommandEnum.DOWN,
        CommandEnum.LEFT,
        CommandEnum.UP,
        CommandEnum.RIGHT
    ]

class BottomRowSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        self.__go_left_center()

    def find_and_replace(self):
        pass

    def __go_left_center(self):
        x, y = self.board.get_coordinates()
        for i in range(x):
            self.__move(CommandEnum.LEFT)
        if y == 2:
            self.__move(CommandEnum.UP)
        elif y == 0:
            self.__move(CommandEnum.DOWN)

    def move_bottom_right(self, self_coordinate, target_coordinate):
        scx = self_coordinate[0]
        tcx = target_coordinate[0]
        for i in range(tcx - scx):
            self.__move(BottomAlgorithm.bottom_right[0])
        for i in range(1, len(BottomAlgorithm.bottom_right)):
            self.__move(BottomAlgorithm.bottom_right[i])

    def move_middle_right(self, self_coordinate, target_coordinate, final_coordinate):
        scx = self_coordinate[0]
        tcx = target_coordinate[0]
        fcx = final_coordinate[0]
        for i in range(tcx - scx):
            self.__move(BottomAlgorithm.middle_right[0])

        for i in range(tcx - fcx - 2):
            for j in range(1, len(BottomAlgorithm.middle_right) - 4):
                self.__move(BottomAlgorithm.middle_right[j])

        for i in range(len(BottomAlgorithm.middle_right) - 4, len(BottomAlgorithm.middle_right)):
            self.__move(BottomAlgorithm.middle_right[i])

    def move_corner_right(self):
        for movement in BottomAlgorithm.corner_right:
            self.__move(movement)

    def middle_left_1_square(self, self_coordinate):
        self.cycle_counter_clockwise(self_coordinate)
        self.__move(CommandEnum.LEFT)
        self.__move(CommandEnum.DOWN)
        self.__move(CommandEnum.RIGHT)
        self.__move(CommandEnum.UP)
        self.cycle_clockwise(self_coordinate)

    def middle_left_2_square(self, self_coordinate):
        self.cycle_counter_clockwise(self_coordinate)
        self.__move(CommandEnum.DOWN)
        self.__move(CommandEnum.LEFT)
        self.__move(CommandEnum.UP)
        self.__move(CommandEnum.RIGHT)
        self.cycle_clockwise(self_coordinate)

    def middle_left_3_square(self, self_coordinate):
        self.cycle_counter_clockwise(self_coordinate)
        self.cycle_counter_clockwise(self_coordinate)
        self.__move(CommandEnum.DOWN)
        self.__move(CommandEnum.LEFT)
        self.__move(CommandEnum.LEFT)
        self.__move(CommandEnum.UP)
        self.__move(CommandEnum.RIGHT)
        self.__move(CommandEnum.DOWN)
        self.__move(CommandEnum.LEFT)
        self.__move(CommandEnum.UP)
        self.__move(CommandEnum.RIGHT)
        self.__move(CommandEnum.RIGHT)
        self.cycle_clockwise(self_coordinate)
        self.cycle_clockwise(self_coordinate)

    def middle_left_4_square(self, self_coordinate):
        self.cycle_counter_clockwise(self_coordinate)
        self.cycle_counter_clockwise(self_coordinate)
        self.__move(CommandEnum.LEFT)
        self.__move(CommandEnum.DOWN)
        self.__move(CommandEnum.LEFT)
        self.__move(CommandEnum.UP)
        self.__move(CommandEnum.RIGHT)
        self.__move(CommandEnum.RIGHT)
        self.cycle_clockwise(self_coordinate)
        self.cycle_clockwise(self_coordinate)

    def cycle_clockwise(self, self_coordinate):
        x = self_coordinate[0]
        for i in range(4 - x):
            self.__move(BottomAlgorithm.cycle_clockwise[0])
        self.__move(BottomAlgorithm.cycle_clockwise[1])
        for i in range(4):
            self.__move(BottomAlgorithm.cycle_clockwise[2])
        self.__move(BottomAlgorithm.cycle_clockwise[3])
        for i in range(x):
            self.__move(BottomAlgorithm.cycle_clockwise[4])

    def cycle_counter_clockwise(self, self_coordinate):
        x = self_coordinate[0]
        for i in range(x):
            self.__move(BottomAlgorithm.cycle_counter_clockwise[0])
        self.__move(BottomAlgorithm.cycle_counter_clockwise[1])
        for i in range(4):
            self.__move(BottomAlgorithm.cycle_counter_clockwise[2])
        self.__move(BottomAlgorithm.cycle_counter_clockwise[3])
        for i in range(4 - x):
            self.__move(BottomAlgorithm.cycle_counter_clockwise[4])

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