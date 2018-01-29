from game_builder.game.abstract_game import AbstractGame


class AutoGame(AbstractGame):
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def move(self):
        raise NotImplementedError

    def display(self):
        raise NotImplementedError
