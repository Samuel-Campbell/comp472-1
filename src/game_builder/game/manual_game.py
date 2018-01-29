from game_builder.game.abstract_game import AbstractGame


class ManualGame(AbstractGame):
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def move(self):
        pass

    def display(self):
        print(self._board[:5])
        print(self._board[5:10])
        print(self._board[-5:])
