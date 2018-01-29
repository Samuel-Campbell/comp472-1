from game_builder.game.abstract_game import AbstractGame


class AutoGame(AbstractGame):
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def run(self):
        raise NotImplementedError

    def _move(self, input_str):
        raise NotImplementedError

    def _display(self):
        raise NotImplementedError
