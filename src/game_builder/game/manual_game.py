from game_builder.game.abstract_game import AbstractGame
from game_builder.game.abstract_game import CommandEnum
from game_builder.board.game_board import GameBoard


class ManualGame(AbstractGame):
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def run(self):
        while not self._game_cleared():
            while True:
                self._display()
                input_str = input('\nEnter you next move. (u, r, d, l)')
                if ManualGame.__validate_input(input_str):
                    self._move(input_str)
                    break
        print("\n++++++++++++++++++++++++++++++++++++++++++")
        self._display()
        print("\n++++++++++++++++++++++++++++++++++++++++++")
        print('You have cleared the game!')

    def _move(self, input_str):
        if input_str == CommandEnum.LEFT:
            GameBoard.move_left()

        elif input_str == CommandEnum.RIGHT:
            GameBoard.move_right()

        elif input_str == CommandEnum.UP:
            GameBoard.move_up()

        elif input_str == CommandEnum.DOWN:
            GameBoard.move_down()

    def _display(self):
        print()
        print(self._board[0])
        print(self._board[1])
        print(self._board[2])

    @staticmethod
    def __validate_input(input_str):
        for variable in CommandEnum.MOVES:
            if variable == input_str:
                return True
        print('invalid input')
        return False
