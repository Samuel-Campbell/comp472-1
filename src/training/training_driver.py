from util.file import File
from training.classifier.linear_svm import LinearSVM
from training.test.test_model import TestModel
from game_builder.difficulty.game_difficulty import GameDifficultyEnum
from training.classifier.naive_bayes import NaiveBayes
from training.classifier.neural_network import NeuralNetwork
from heuristics.depth_first_search import depth_first_search_driver
from util.file import File


def __train_svm(binary_model):
    model = File.load_binary(binary_model)
    svm = LinearSVM(model)
    svm.train()


def __train_naive_bayes(binary_model):
    model = File.load_binary(binary_model)
    nb = NaiveBayes(model)
    nb.train()


def __train_neural_network(binary_model, binary_name):
    model = File.load_binary(binary_model)
    nn = NeuralNetwork(model)
    nn.train()
    nn.save(binary_name)


def __evaluate(binary_model):
    model = File.load_binary(binary_model)
    nn = NeuralNetwork(model)
    nn.evaluate_best_parameters()


def optimize():
    depth_first_search_driver.run_premade_boards('novice_data.bin', 'novice_model.bin', 10)
    __train_neural_network('novice_data.bin', 'novice_model.bin')


def run():
    max_steps = 10
    for i in range(5):
        print('Training Iteration: {}'.format(str(i)))
        max_steps = depth_first_search_driver.run(GameDifficultyEnum.NOVICE,'novice_data.bin',
                                      1000, 'novice_model.bin', max_steps)
        max_steps += int(max_steps * 0.2)
        __train_neural_network('novice_data.bin', 'novice_model.bin')

    max_steps = 15
    for i in range(5):
        print('Training Iteration: {}'.format(str(i)))
        max_steps = depth_first_search_driver.run(GameDifficultyEnum.APPRENTICE,'apprentice_data.bin',
                                      1000, 'apprentice_model.bin', max_steps)
        max_steps += int(max_steps * 0.2)
        __train_neural_network('apprentice_data.bin', 'apprentice_model.bin')

    max_steps = 20
    for i in range(5):
        print('Training Iteration: {}'.format(str(i)))
        max_steps = depth_first_search_driver.run(GameDifficultyEnum.EXPERT,'expert_data.bin',
                                      1000, 'expert_model.bin', max_steps)
        max_steps += int(max_steps * 0.2)
        __train_neural_network('expert_data.bin', 'expert_model.bin')

    max_steps = 25
    for i in range(5):
        print('Training Iteration: {}'.format(str(i)))
        max_steps = depth_first_search_driver.run(GameDifficultyEnum.MASTER,'master_data.bin',
                                      1000, 'master_model.bin', max_steps)
        max_steps += int(max_steps * 0.2)
        __train_neural_network('master_data.bin', 'master_model.bin')
