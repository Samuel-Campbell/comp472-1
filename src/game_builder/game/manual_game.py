from game_builder.game.abstract_game import AbstractGame
from game_builder.game.abstract_game import CommandEnum


class ManualGame(AbstractGame):
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def run(self):
        """
        runs the game on manual mode

        1) While the game isn't completed, accept a user's inputs
        2) Validate the user's inputs. If not correct then re-prompt
        3) If user's input is valid then move on the board
        4) When the game is cleared the return a success message to the command line

        :return: None
        """

        while not self._board.game_cleared():
            while True:
                self._board.display()
                input_str = input('\nEnter you next move. (w (up), d (right), s (down), a (left)')
                if ManualGame.__validate_input(input_str):
                    self._move(input_str)
                    break
        print("\n++++++++++++++++++++++++++++++++++++++++++")
        self._board.display()
        print("\n++++++++++++++++++++++++++++++++++++++++++")
        print('You have cleared the game!')

    @staticmethod
    def __validate_input(input_str):
        """
        Validates the input string of the user

        1) Iterate CommandEnum list
        2) if iterated variable matches input_str then return True
        3) else return False if no matches are found

        :param input_str: string
        :return: boolean
        """

        for variable in CommandEnum.MOVES:
            if variable == input_str:
                return True
        print('invalid input')
        return False
