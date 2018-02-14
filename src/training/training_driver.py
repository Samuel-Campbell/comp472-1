from training.classifier.linear_svm import LinearSVM
from training.classifier.naive_bayes import NaiveBayes
from training.regression.neural_network import NeuralNetwork
# from training.regression.deep_learning import DeepLearner
from game_builder.difficulty.game_difficulty import GameDifficultyEnum
from heuristics.reverse_solver import reverse_solver_driver
from util.file import File


def __train_svm(binary_model, binary_name):
    model = File.load_binary(binary_model)
    svm = LinearSVM(model)
    svm.train()


def __train_naive_bayes(binary_model):
    model = File.load_binary(binary_model)
    nb = NaiveBayes(model)
    nb.train()


def __train_neural_network(binary_data_points, binary_name):
    model = File.load_binary(binary_data_points)
    nn = NeuralNetwork(model)
    nn.train()
    nn.save(binary_name)



def __train_deep_learning(binary_data_points, binary_name):
    model = File.load_binary(binary_data_points)
    dl = DeepLearner(model)
    dl.train()



def __evaluate(binary_model):
    model = File.load_binary(binary_model)
    nn = NeuralNetwork(model)
    nn.evaluate_best_parameters()


def run():
    steps = 5
    while steps <= 200:
        reverse_solver_driver.run('novice_data.bin', steps, GameDifficultyEnum.NOVICE, 1000)
        __train_neural_network('novice_data.bin', 'novice_model.bin')
        steps += 10
    #__evaluate('novice_data.bin')
