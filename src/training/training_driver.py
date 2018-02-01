from util.file import File
from training.classifier.linear_svm import LinearSVM
from training.test.test_model import TestModel
from game_builder.difficulty.game_difficulty import GameDifficultyEnum
from training.classifier.naive_bayes import NaiveBayes
from training.classifier.neural_network import NeuralNetwork
from heuristics.depth_first_search import depth_first_search_driver
from util.file import File


def train_svm(binary_model):
    model = File.load_binary(binary_model)
    svm = LinearSVM(model)
    svm.train()


def train_naive_bayes(binary_model):
    model = File.load_binary(binary_model)
    nb = NaiveBayes(model)
    nb.train()


def train_neural_network(binary_model, binary_name):
    model = File.load_binary(binary_model)
    nn = NeuralNetwork(model)
    nn.train()
    nn.save(binary_name)

if __name__ == '__main__':
    model = File.load_binary('novice_data.bin')
    c = 0
    for key in model:
        print(model[key])
        c +=1
        if c == 100:
            break
    """
    max_steps = 0
    for i in range(5):        
        print('Training Iteration: {}'.format(str(i)))
        max_steps = depth_first_search_driver.run(GameDifficultyEnum.APPRENTICE,'apprentice_data.bin',
                                      2000, 'apprentice_model.bin', max_steps)
        max_steps += int(max_steps * 0.5)
        train_neural_network('apprentice_data.bin', 'apprentice_model.bin')    

    max_steps = 0
    for i in range(20):
        print('Training Iteration: {}'.format(str(i)))
        max_steps = depth_first_search_driver.run(GameDifficultyEnum.EXPERT,'expert_data.bin',
                                      100, 'expert_model.bin', max_steps)
        max_steps += int(max_steps * 0.25)
        train_neural_network('expert_data.bin', 'expert_model.bin')
    """
    """
    max_steps = 0
    for i in range(20):
        print('Training Iteration: {}'.format(str(i)))
        max_steps = depth_first_search_driver.run(GameDifficultyEnum.MASTER,'master_data.bin',
                                      200, 'master_model.bin', max_steps)
        max_steps += int(max_steps * 0.1)
        train_neural_network('master_data.bin', 'master_model.bin')
    """
    """
    max_steps = 0
    for i in range(5):        
        print('Training Iteration: {}'.format(str(i)))
        max_steps = depth_first_search_driver.run(GameDifficultyEnum.NOVICE,'novice_data.bin',
                                      2000, 'novice_model.bin', max_steps)
        max_steps += int(max_steps * 0.5)
        train_neural_network('novice_data.bin', 'novice_model.bin')
    """