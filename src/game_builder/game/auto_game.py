from game_builder.game.abstract_game import AbstractGame
from training.classifier.linear_svm import LinearSVM
import time


class AutoGame(AbstractGame):
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def run(self):
        svm = LinearSVM(None)
        steps = 0
        while not self._board.game_cleared():
            input_str = svm.predict(self._board.get_board_state())
            self._move(input_str)
            self._board.display()
            steps += 1
            time.sleep(1)
        print('Auto Clear in {} Steps'.format(str(steps)))