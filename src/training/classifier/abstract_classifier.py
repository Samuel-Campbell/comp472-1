import numpy as np
from util.file import File


class AbstractClassifier:

    int_to_move = {
        0: 'u',
        1: 'd',
        2: 'r',
        3: 'l'
    }

    def __init__(self, dataset):
        self.dataset = dataset
        self.model = None

    def train(self):
        raise NotImplementedError

    def test(self, x_test, y_test):
        raise NotImplementedError

    def predict(self, data):
        if self.model is None:
            self.model = File.load_binary('novice_model.bin')
        data = [data]
        print(self.model.predict_proba(data))
        prediction = self.model.predict(data)
        return self.int_to_move[prediction[0]]

    def predict_probabilities(self, data):
        if self.model is None:
            self.model = File.load_binary('novice_model.bin')
        data = [data]
        prediction = self.model.predict_proba(data)[0]
        return_pred = []
        for i in range(len(prediction)):
            return_pred.append([prediction[i], self.int_to_move[i]])
        return return_pred

    def reshape_dataset(self):
        x_total = []
        y_total = []
        for permutation in self.dataset:
            x_total.append(self.dataset[permutation][0])
            y_total.append(self.dataset[permutation][1])
        x_total = np.array(x_total)
        y_total = np.array(y_total)
        return x_total , y_total