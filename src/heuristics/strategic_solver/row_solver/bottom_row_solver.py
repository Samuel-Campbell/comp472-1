from game_builder.game.abstract_game import CommandEnum
from heuristics.strategic_solver.row_solver.abstract_row_solver import AbstractRowSolver


class BottomAlgorithm:
    bottom_right = [
        CommandEnum.RIGHT,
        CommandEnum.DOWN,
        CommandEnum.LEFT,
        CommandEnum.UP
    ]

    middle_right = [
        CommandEnum.RIGHT,
        CommandEnum.DOWN,
        CommandEnum.LEFT,
        CommandEnum.LEFT,
        CommandEnum.LEFT,
        CommandEnum.UP,
        CommandEnum.RIGHT,
        CommandEnum.RIGHT,
        CommandEnum.DOWN,
        CommandEnum.LEFT,
        CommandEnum.LEFT,
        CommandEnum.UP
    ]

    corner_top_right = [
        CommandEnum.DOWN,
        CommandEnum.RIGHT,
        CommandEnum.UP,
        CommandEnum.LEFT,
        CommandEnum.DOWN,
        CommandEnum.RIGHT,
        CommandEnum.UP,
        CommandEnum.LEFT
    ]

    corner_bottom_right = [
        CommandEnum.DOWN,
        CommandEnum.RIGHT,
        CommandEnum.UP,
        CommandEnum.LEFT
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


class BottomRowSolver(AbstractRowSolver):
    def __init__(self, board, verbose=False, output=False):
        AbstractRowSolver.__init__(self, board, verbose, output)

    def solve(self):
        self._go_left_center()
        self_coordinate = 0
        for i in range(5):
            game_state = self.board.get_board_state()
            answer = [i for i, j in enumerate(game_state) if j == game_state[self_coordinate]]
            for j in range(len(answer) - 1, -1, -1):
                # if top row ignore
                if answer[j] < 5:
                    pass

                # if to the right
                elif (answer[j] % 5) > self_coordinate:
                    answer = [answer[j] % 5, int(answer[j] / 5)]
                    break

                # if to the left and middle row
                elif ((answer[j] % 5) < self_coordinate) and (int(answer[j] / 5) == 1):
                    answer = [answer[j] % 5, int(answer[j] / 5)]
                    break

            if game_state[self_coordinate] == game_state[i + 10]:
                pass

            elif (answer[1] == 2) and (answer[0] > (self_coordinate + 1)):
                self.move_bottom_right([self_coordinate, 1], answer, [self_coordinate, 2])

            elif (answer[1] == 1) and (answer[0] > (self_coordinate + 1)):
                self.move_middle_right([self_coordinate, 1], answer, [self_coordinate, 2])

            elif (answer[1] == 1) and (answer[0] == (self_coordinate + 1)):
                self.move_corner_right()

            elif (answer[1] == 2) and (answer[0] == (self_coordinate + 1)):
                self.move_corner_bottom_right()

            elif answer[0] == self_coordinate -1:
                self.middle_left_1_square([self_coordinate, 1])

            elif answer[0] == self_coordinate -2:
                self.middle_left_2_square([self_coordinate, 1])

            elif answer[0] == self_coordinate -3:
                self.middle_left_3_square([self_coordinate, 1])

            elif answer[0] == self_coordinate -4:
                self.middle_left_4_square([self_coordinate, 1])

            self_coordinate += 1
            if self_coordinate < 4:
                self._move(CommandEnum.RIGHT)

    def move_bottom_right(self, self_coordinate, target_coordinate, final_coordinate):
        scx = self_coordinate[0]
        tcx = target_coordinate[0]
        for i in range(tcx - scx):
            self._move(BottomAlgorithm.bottom_right[0])
        for i in range(1, len(BottomAlgorithm.bottom_right)):
            self._move(BottomAlgorithm.bottom_right[i])
        self_coordinate[0] = tcx - 1
        self.move_middle_right(self_coordinate, target_coordinate, final_coordinate)

    def move_middle_right(self, self_coordinate, target_coordinate, final_coordinate):
        scx = self_coordinate[0]
        tcx = target_coordinate[0]
        fcx = final_coordinate[0]
        for i in range(tcx - scx):
            self._move(BottomAlgorithm.middle_right[0])

        for i in range(tcx - fcx - 2):
            for j in range(1, len(BottomAlgorithm.middle_right) - 4):
                self._move(BottomAlgorithm.middle_right[j])

        for i in range(len(BottomAlgorithm.middle_right) - 4, len(BottomAlgorithm.middle_right)):
            self._move(BottomAlgorithm.middle_right[i])
        self.move_corner_right()

    def move_corner_right(self):
        for movement in BottomAlgorithm.corner_top_right:
            self._move(movement)

    def move_corner_bottom_right(self):
        for movement in BottomAlgorithm.corner_bottom_right:
            self._move(movement)

    # REVIEW THIS TO DO
    def middle_left_1_square(self, self_coordinate):
        if self_coordinate[0] > 1:
            self.cycle_counter_clockwise(self_coordinate)
            self._move(CommandEnum.LEFT)
            self._move(CommandEnum.DOWN)
            self._move(CommandEnum.RIGHT)
            self._move(CommandEnum.UP)
            self.cycle_clockwise(self_coordinate)
        else:
            self._move(CommandEnum.RIGHT)
            self_coordinate[0] += 1
            self.middle_left_2_square(self_coordinate)
            self._move(CommandEnum.LEFT)
            self._move(CommandEnum.DOWN)
            self._move(CommandEnum.RIGHT)
            self._move(CommandEnum.UP)
            self._move(CommandEnum.LEFT)


    def middle_left_2_square(self, self_coordinate):
        self.cycle_counter_clockwise(self_coordinate)
        self._move(CommandEnum.DOWN)
        self._move(CommandEnum.LEFT)
        self._move(CommandEnum.UP)
        self._move(CommandEnum.RIGHT)
        self.cycle_clockwise(self_coordinate)

    def middle_left_3_square(self, self_coordinate):
        self.cycle_counter_clockwise(self_coordinate)
        self.cycle_counter_clockwise(self_coordinate)
        self._move(CommandEnum.DOWN)
        self._move(CommandEnum.LEFT)
        self._move(CommandEnum.UP)
        self._move(CommandEnum.RIGHT)
        self.cycle_clockwise(self_coordinate)
        self._move(CommandEnum.LEFT)
        self._move(CommandEnum.DOWN)
        self._move(CommandEnum.RIGHT)
        self._move(CommandEnum.UP)
        self.cycle_clockwise(self_coordinate)

    def middle_left_4_square(self, self_coordinate):
        self.cycle_counter_clockwise(self_coordinate)
        self.cycle_counter_clockwise(self_coordinate)
        self._move(CommandEnum.LEFT)
        self._move(CommandEnum.DOWN)
        self._move(CommandEnum.LEFT)
        self._move(CommandEnum.UP)
        self._move(CommandEnum.RIGHT)
        self._move(CommandEnum.RIGHT)
        self.cycle_clockwise(self_coordinate)
        self.cycle_clockwise(self_coordinate)

    # END OF REVIEW

    def cycle_clockwise(self, self_coordinate):
        x = self_coordinate[0]
        self._move(CommandEnum.DOWN)
        for i in range(x):
            self._move(CommandEnum.LEFT)
        self._move(CommandEnum.UP)
        for i in range(x):
            self._move(CommandEnum.RIGHT)

    def cycle_counter_clockwise(self, self_coordinate):
        x = self_coordinate[0]
        for i in range(x):
            self._move(CommandEnum.LEFT)
        self._move(CommandEnum.DOWN)
        for i in range(x):
            self._move(CommandEnum.RIGHT)
        self._move(CommandEnum.UP)


