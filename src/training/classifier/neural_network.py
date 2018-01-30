from training.classifier.abstract_classifier import AbstractClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from util.file import File
from sklearn.neural_network import MLPClassifier


class NeuralNetwork(AbstractClassifier):
    def __init__(self, dataset):
        AbstractClassifier.__init__(self, dataset)
        self.model = None

    def train(self):
        """

        """
        (x_total, y_total) = self.reshape_dataset()
        x_train, x_test, y_train, y_test = train_test_split(
            x_total, y_total, test_size=0.20, random_state=42)
        print("Sample size: {}".format(len(x_total)))
        print("Train size: {}".format(len(x_train)))
        print("Test size: {}".format(len(x_test)))

        print("Training Classifier using Linear SVM")
        clf = MLPClassifier()
        self.model = clf.fit(x_train, y_train)
        self.test(x_test, y_test)
        File.save_binary('novice_model.bin', self.model)

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

        parameters = {'activation': ('identity', 'logistic', 'tanh',
                                 'relu'),
                      'solver': ('lbfgs', 'sgd', 'adam'),
                      ' hidden_layer_sizes': ((100,), (5,), (7,))
                      }

        nn = MLPClassifier()
        clf = GridSearchCV(nn, parameters)
        clf.fit(x_train, y_train)
        return clf.best_params_


