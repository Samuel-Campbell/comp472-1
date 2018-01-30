import os
import joblib


class File:
    def __init__(self):
        pass

    @staticmethod
    def load_binary(filename):
        """
        returns binarized model
        :param filename: name of file to load
        :return: None
        """
        try:
            print("Loading " + filename)
            root_directory = os.path.abspath(__file__ + "r/../../")
            rel_path = r'data/binary/' + filename
            file_path = os.path.join(root_directory, rel_path)
            file = open(file_path, "rb")
            binary = joblib.load(file)
            print(filename + " is successfully loaded")
            return binary
        except BaseException:
            print('File not found')


    @staticmethod
    def save_binary(filename, model):
        """
        saves a binary model
        :return: None
        """
        root_directory = os.path.abspath(__file__ + "r/../../")
        rel_path = r'data/binary/' + filename
        file_path = os.path.join(root_directory, rel_path)
        print("saving " + filename + " to: " + file_path)
        joblib.dump(model, file_path)
        print(filename + " saved to: " + file_path)
