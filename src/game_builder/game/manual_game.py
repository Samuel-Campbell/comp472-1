from game_builder.game.abstract_game import AbstractGame
from game_builder.game.abstract_game import CommandEnum
from game_builder.board.game_board import GameBoard


class ManualGame(AbstractGame):
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def run(self):
        while not self._board.game_cleared():
            while True:
                self._board.display()
                input_str = input('\nEnter you next move. (u, r, d, l)')
                if ManualGame.__validate_input(input_str):
                    self._move(input_str)
                    break
        print("\n++++++++++++++++++++++++++++++++++++++++++")
        self._board.display()
        print("\n++++++++++++++++++++++++++++++++++++++++++")
        print('You have cleared the game!')

    def _move(self, input_str):
        if input_str == CommandEnum.LEFT:
            self._board.move_left()

        elif input_str == CommandEnum.RIGHT:
            self._board.move_right()

        elif input_str == CommandEnum.UP:
            self._board.move_up()

        elif input_str == CommandEnum.DOWN:
            self._board.move_down()

    @staticmethod
    def __validate_input(input_str):
        for variable in CommandEnum.MOVES:
            if variable == input_str:
                return True
        print('invalid input')
        return False
