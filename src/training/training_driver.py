from util.file import File
from training.classifier.linear_svm import LinearSVM
from training.test.test_model import TestModel
from game_builder.difficulty.game_difficulty import GameDifficultyEnum
from training.classifier.naive_bayes import NaiveBayes
from training.classifier.neural_network import NeuralNetwork
from heuristics.depth_first_search import depth_first_search_driver


def train_svm(binary_model):
    model = File.load_binary(binary_model)
    svm = LinearSVM(model)
    svm.evaluate_best_parameters()


def train_naive_bayes(binary_model):
    model = File.load_binary(binary_model)
    nb = NaiveBayes(model)
    nb.train()


def train_neural_network(binary_model):
    model = File.load_binary(binary_model)
    nn = NeuralNetwork(model)
    nn.train()


if __name__ == '__main__':
    for i in range(5):
        print('Training Iteration: {}'.format(str(i)))
        depth_first_search_driver.run(GameDifficultyEnum.NOVICE,'novice_data.bin',
                                      2000, 'novice_model.bin')
        train_neural_network('novice_data.bin')

    for i in range(5):
        print('Training Iteration: {}'.format(str(i)))
        depth_first_search_driver.run(GameDifficultyEnum.APPRENTICE,'apprentice_data.bin',
                                      2000, 'apprentice_model.bin')
        train_neural_network('apprentice_data.bin')

    for i in range(5):
        print('Training Iteration: {}'.format(str(i)))
        depth_first_search_driver.run(GameDifficultyEnum.EXPERT,'expert_data.bin',
                                      2000, 'expert_model.bin')
        train_neural_network('expert_data.bin')

    for i in range(5):
        print('Training Iteration: {}'.format(str(i)))
        depth_first_search_driver.run(GameDifficultyEnum.MASTER,'master_data.bin',
                                      2000, 'master_model.bin')
        train_neural_network('master_data.bin')