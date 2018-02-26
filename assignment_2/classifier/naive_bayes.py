def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix
import numpy


class NaiveBayes:
    def __init__(self, training_set, test_set, smoothing=False):
        """
        :param training_set: list[list] -->  [['class', 'data], ['class', 'data'], ...]
        :param test_set: list[list] -->  [['class', 'data], ['class', 'data'], ...]
        :param smoothing: bool
        """
        self.training_set = training_set
        self.test_set = test_set
        self.smoothing = smoothing
        self.clf = None
        self.vectorizer = None

    def train(self):
        """
        1) reshape data
        2) if smoothing apply it
        3) fit classifier

        :return: None
        """
        X, Y = self.__reshape_data()
        if self.smoothing:
            self.clf = MultinomialNB(alpha=0.5)
        else:
            self.clf = MultinomialNB(alpha=0.0)
        self.clf.fit(X, Y)

    def test(self):
        """
        1) split data from results
        2) vectorize data
        3) obtain predicted results
        4) Accuracy
        5) Precision
        6) Recall
        7) F1
        8) Confusion Matrix
        9) all sentences and their predictions

        :return: None
        """
        X_test = [x[0] for x in self.test_set]
        X_test = self.vectorizer.transform(X_test).toarray()
        y_predict = self.clf.predict(X_test)
        y_true = [y[1] for y in self.test_set]
        num_correct = numpy.sum(y_predict == y_true)
        (precision, recall, f1, _) = precision_recall_fscore_support(y_true, y_predict)
        cm = confusion_matrix(y_true, y_predict)
        print('Test accuracy: {0:.2f}%'.format(num_correct * 100.0 / len(y_true)))
        print('Precision: {}'.format(precision))
        print('Recall: {}'.format(recall))
        print('F1: {}'.format(f1))
        print('Confusion Matrix:')
        print(cm)
        print("\nPredictions: ")
        for sent in self.test_set:
            x = self.vectorizer.transform([sent[0]]).toarray()
            prediction = self.clf.predict(x)
            sentence = sent[0].replace('\n', '')
            print(sentence, prediction)

    def __reshape_data(self):
        """
        This uses a word count vectorizer since the dictionary of words is so small
        else we would use word vectors.

        1) split input data from results
        2) Create the vectorizer model
        3) vectorize the training set

        :return: list[list], list[list]
        """
        X_train = [x[0] for x in self.training_set]
        Y_train = [y[1] for y in self.training_set]
        self.vectorizer = CountVectorizer().fit(X_train)
        X_train = self.vectorizer.transform(X_train).toarray()
        return X_train, Y_train
