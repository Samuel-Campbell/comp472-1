from util.file import File
from training.classifier.linear_svm import LinearSVM
from training.test.test_model import TestModel
from game_builder.difficulty.game_difficulty import GameDifficultyEnum
from training.classifier.naive_bayes import NaiveBayes


def train_svm():
    novice_model = File.load_binary('novice_random.bin')
    svm = LinearSVM(novice_model)
    svm.train()


def train_naive_bayes():
    novice_model = File.load_binary('novice_random.bin')
    nb = NaiveBayes(novice_model)
    nb.train()


if __name__ == '__main__':
    train_naive_bayes()
    #TestModel.solve_puzzle(GameDifficultyEnum.NOVICE)
