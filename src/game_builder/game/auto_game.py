from game_builder.game.abstract_game import AbstractGame
from training.classifier.abstract_classifier import AbstractClassifier
import time
from util.file import File
from game_builder.difficulty.game_difficulty import GameDifficultyEnum


class AutoGame(AbstractGame):
    move_to_int = {
        0: 'w',
        1: 's',
        2: 'd',
        3: 'a'
    }

    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def run(self):
        clf = AbstractClassifier(None).model
        if self._board.difficulty == GameDifficultyEnum.NOVICE:
            clf = File.load_binary('novice_model.bin')
        elif self._board.difficulty == GameDifficultyEnum.APPRENTICE:
            clf = File.load_binary('apprentice_model.bin')
        elif self._board.difficulty == GameDifficultyEnum.EXPERT:
            clf = File.load_binary('expert_model.bin')
        elif self._board.difficulty == GameDifficultyEnum.MASTER:
            clf = File.load_binary('master_model.bin')
        steps = 0
        while not self._board.game_cleared():
            input_str = clf.predict([self._board.get_board_state()])
            next_move = self.move_to_int[input_str[0]]
            self._move(next_move)
            self._board.display()
            steps += 1
            time.sleep(1)
        print('Auto Clear in {} Steps'.format(str(steps)))
