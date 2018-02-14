from training.regression.abstract_regressor import AbstractRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from util.file import File
from sklearn.neural_network import MLPRegressor


class NeuralNetwork(AbstractRegressor):
    def __init__(self, dataset):
        AbstractRegressor.__init__(self, dataset)

    def train(self):
        """

        """
        x_total, y_total = self.reshape_dataset()
        x_train, x_test, y_train, y_test = train_test_split(
            x_total, y_total, test_size=0.20, random_state=42)
        print("Sample size: {}".format(len(x_total)))
        print("Train size: {}".format(len(x_train)))
        print("Test size: {}".format(len(x_test)))

        print("Training Regression using Neural Networks")
        clf = MLPRegressor()
        self.model = clf.fit(x_train, y_train)
        self.test(x_test, y_test)

    def test(self, x_test, y_test):
        # Test
        print("Testing Classifier")
        y_predict = self.model.predict(x_test)
        mse = mean_squared_error(y_test, y_predict)
        r2 = r2_score(y_test, y_predict)
        print('Mean Squared Error: {}'.format(mse))
        print('R2: {}'.format(r2))

    def evaluate_best_parameters(self):
        """
        Evaluate several different parameter combinations and
        returns the best combination.
        returns: a dict containing the most optimal parameter
                 combination
        """
        x_total, y_total = self.reshape_dataset()
        x_total = x_total[:1000]
        y_total = y_total[:1000]
        x_train, x_test, y_train, y_test = train_test_split(
            x_total, y_total, test_size=0.20, random_state=42)

        parameters = {
            'momentum': (0.4, 0.5, 0.6),
        }

        nn = MLPRegressor(
            activation='relu', solver='sgd', max_iter=1000, nesterovs_momentum=True, learning_rate='adaptive')
        clf = GridSearchCV(nn, parameters)
        clf.fit(x_train, y_train)
        print(clf.best_params_)


