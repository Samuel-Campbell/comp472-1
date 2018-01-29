class AbstractGame:
    def __init__(self, board):
        self._board = board

    def move(self):
        raise NotImplementedError

    def display(self):
        raise NotImplementedError

    def game_cleared(self):
        if self._board[:5] == self._board[-5:]:
            return True
        return False
