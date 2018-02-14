from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from training.classifier.abstract_classifier import AbstractClassifier
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np
from util.file import File


class DeepLearner(AbstractClassifier):

    def __init__(self, dataset):
        AbstractClassifier.__init__(self, dataset)
        self.scaler = None

    @staticmethod
    def __nn_architecture():
        """
            Defines Regressor architecture. To be used internally
        """
        model = Sequential()
        model.add(Dense(10, input_dim=15,
                        kernel_initializer='normal', activation='relu'))
        model.add(Dense(4, kernel_initializer='normal', activation='relu'))
        model.add(Dense(1, kernel_initializer='normal'))
        model.compile(loss='mean_absolute_percentage_error', optimizer='adam')
        return model

    def train(self):
        """
            Trains the pipeline. After training the dataset is removed
            from the object to save space.
        """
        x_total, y_total = self.reshape_dataset()
        x_train, x_test, y_train, y_test = train_test_split(
            x_total[:10000], y_total[:10000], test_size=0.20, random_state=42)

        print("Sample size: {}".format(len(x_total)))
        print("Train size: {}".format(len(x_train)))
        print("Test size: {}".format(len(x_test)))

        regressor = KerasRegressor(
            build_fn=DeepLearner.__nn_architecture, epochs=150, batch_size=128, verbose=0
        )
        self.scaler = StandardScaler()
        self.model = DeepLearner.__create_pipeline(self.scaler, regressor)
        self.model.fit(x_train, y_train)
        self.test(x_test, y_test)

    @staticmethod
    def __create_pipeline(scaler, regressor):
        """
            Creates the pipeline of scaler + regressor
            and returns it.
        """
        estimators = []
        estimators.append(('standardize', scaler))
        estimators.append(('mlp', regressor))

        return Pipeline(estimators)

    def test(self, x, y):
        """
            Tests the regressor using the dataset and writes
            the mean and MSE of the deviation
        """
        seed = 7
        np.random.seed(seed)
        kfold = KFold(n_splits=10, random_state=seed)
        results = cross_val_score(self.model, x, y, cv=kfold)
        print("Mean: %.2f (%.2f) MSE" % (results.mean(), results.std()))