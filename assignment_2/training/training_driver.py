import os
from classifier.naive_bayes import NaiveBayes


def __parse_set(filename):
    """
    Iterates every line of the file and splits it where it finds a \t or \s\s
    1) First term is the class
    2) Second term is the data
    :param filename: name of the file
    :return: list[list] --> [['class', 'data], ['class', 'data'], ...]
    """
    data_set = []
    file = open(filename, 'r')
    for line in file:
        data = line.split('\t')
        if len(data) == 1:
            data = line.split('  ')
        y = data[0]
        x = data[1]
        data_set.append([x, y])
    file.close()
    return data_set


def train_naive_bayes():
    """
    Trains with naive bayes using smoothing = 0.5 and non-smoothing
    Test set and training set is separated in 2 different files beforehand

    :return: None
    """
    data_path = os.path.abspath(__file__ + "r/../../data")
    train_file = os.path.join(data_path, 'training.txt')
    test_file = os.path.join(data_path, 'testing.txt')

    training_set = __parse_set(train_file)
    test_set = __parse_set(test_file)

    print("Training using no smoothing")
    nb = NaiveBayes(training_set, test_set)
    nb.train()
    nb.test()

    print("\nTraining using smoothing: 0.5")
    nb = NaiveBayes(training_set, test_set, smoothing=True)
    nb.train()
    nb.test()
