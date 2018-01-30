from util.file import File
from training.classifier.linear_svm import LinearSVM
from training.test.test_model import TestModel
from game_builder.difficulty.game_difficulty import GameDifficultyEnum
from training.classifier.naive_bayes import NaiveBayes
from training.classifier.neural_network import NeuralNetwork


def train_svm():
    novice_model = File.load_binary('novice_random.bin')
    svm = LinearSVM(novice_model)
    svm.evaluate_best_parameters()


def train_naive_bayes():
    novice_model = File.load_binary('novice_random.bin')
    nb = NaiveBayes(novice_model)
    nb.train()


def train_neural_network():
    novice_model = File.load_binary('novice_dfs.bin')
    nn = NeuralNetwork(novice_model)
    nn.train()


if __name__ == '__main__':
    #train_neural_network()
    TestModel.solve_puzzle(GameDifficultyEnum.NOVICE)
