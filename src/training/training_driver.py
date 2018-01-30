from util.file import File
from training.classifier.linear_svm import LinearSVM
from training.test.test_model import TestModel
from game_builder.difficulty.game_difficulty import GameDifficultyEnum


if __name__ == '__main__':
    novice_model = File.load_binary('novice_random.bin')
    svm = LinearSVM(novice_model)
    svm.train()
    #TestModel.solve_puzzle(GameDifficultyEnum.NOVICE)
