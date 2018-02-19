import numpy as np
from util.file import File


class AbstractRegressor:

    int_to_move = {
        0: 'u',
        1: 'd',
        2: 'r',
        3: 'l'
    }

    def __init__(self, dataset):
        """
        Constructor
        :param dataset: classifier model
        """
        self.dataset = dataset
        self.model = None
        self.decay_dict = {}

    def train(self):
        raise NotImplementedError

    def test(self, x_test, y_test):
        raise NotImplementedError

    def predict(self, data):
        """
        Predicts the next best move depending on the board state

        :param data: board state np.array([1, 2, 3, 4...])
        :return: prediction <int> [0, 3] -- each number representing a move
        """
        data = [data]
        prediction = self.model.predict(data)
        return self.int_to_move[prediction[0]]

    def predict_probabilities(self, data):
        """
        :param data: numpy.array([1, 2, 3, 3, ...])
        :return:
            [[float, str], [float, str], [float, str], [float, str]]
            [[Probability of best move, move]]
        """
        data = [data]
        prediction = self.model.predict_proba(data)[0]
        return_pred = []
        for i in range(len(prediction)):
            return_pred.append([prediction[i], self.int_to_move[i]])
        return return_pred

    def reshape_dataset(self):
        """
        Reshape the dataset into inputs: x and outputs: y

        every value in the dictionary contains the following:
        board state, next best move, moves to completion
        [numpy.array([]), int, int]

        **For now we are only interested in the board state and the next best move.
          This is still experimental.

        :return: None
        """
        x_total = []
        y_total = []
        for permutation in self.dataset:
            lst = list(self.dataset[permutation][0])
            lst.append(self.dataset[permutation][1])
            lst.append(self.dataset[permutation][2])
            x_total.append(np.array(lst))
            y_total.append(self.dataset[permutation][4])
        x_total = np.array(x_total)
        y_total = np.array(y_total)
        return x_total , y_total

    def save(self, filename):
        """
        Saves the model as a binary

        :param filename: name of the file
        :return: None
        """
        File.save_binary(filename, self.model)