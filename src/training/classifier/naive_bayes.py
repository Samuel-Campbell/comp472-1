from training.classifier.abstract_classifier import AbstractClassifier
from util.file import File
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
from sklearn.naive_bayes import GaussianNB
import numpy as np


class NaiveBayes(AbstractClassifier):
    def __init__(self, dataset):
        AbstractClassifier.__init__(self, dataset)
        self.model = None

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

        print("Using Naive Bayes")
        clf = GaussianNB()
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
