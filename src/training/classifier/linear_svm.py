from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from util.file import File


class LinearSVM:

    int_to_move = {
        0: 'u',
        1: 'd',
        2: 'r',
        3: 'l'
    }

    def __init__(self, dataset):
        self.dataset = dataset
        self.model = None

    def predict(self, data):
        if self.model is None:
            self.model = File.load_binary('novice_svm.bin')
        data = [data]
        prediction = self.model.predict(data)
        return self.int_to_move[prediction[0]]

    def train(self):
        """
            Trains the Linear Support Vector Machine.
        """
        (x_total, y_total) = self.reshape_dataset()
        x_train, x_test, y_train, y_test = train_test_split(
            x_total, y_total, test_size=0.20, random_state=42)
        print("Sample size: {}".format(len(x_total)))
        print("Train size: {}".format(len(x_train)))
        print("Test size: {}".format(len(x_test)))

        print("Training Classifier using Linear SVM")
        clf = svm.SVC(kernel='poly', random_state=42, C=3, probability=True)
        self.model = clf.fit(x_train, y_train)
        self.test(x_test, y_test)
        File.save_binary('novice_svm.bin', self.model)


    def test(self, x_test, y_test):
        # Test
        print("Testing Classifier")
        y_predict = self.model.predict(x_test)
        num_correct = np.sum(y_predict == y_test)
        (precision, recall, f1, _) = precision_recall_fscore_support(y_test, y_predict)
        print('Test accuracy: {}%'.format(
            num_correct * 100.0 / len(y_test)))
        print('Precision: {}'.format(precision))
        print('Recall: {}'.format(recall))
        print('F1: {}'.format(f1))

    def evaluate_best_parameters(self):
        """
            Evaluate several different parameter combinations and
            returns the best combination.
            returns: a dict containing the most optimal parameter
                     combination
        """
        (x_total, y_total) = self.reshape_dataset()
        x_train, x_test, y_train, y_test = train_test_split(
            x_total, y_total, test_size=0.20, random_state=42)

        parameters = {'kernel': ('linear', 'poly', 'sigmoid',
                                 'rbf'),
                      'C': [0.7, 3, 4, 5]
                      }

        svc = svm.SVC()
        clf = GridSearchCV(svc, parameters)
        clf.fit(x_train, y_train)
        return clf.best_params_

    def reshape_dataset(self):
        x_total = []
        y_total = []

        for permutation in self.dataset:
            for step in self.dataset[permutation]:
                x = []
                for board_state in step[0]:
                    x += (list(board_state))
                x_total.append(x)
                y_total.append(step[1])

        x_total = np.array(x_total)
        y_total = np.array(y_total)
        return x_total , y_total