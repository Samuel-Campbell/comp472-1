import os
import joblib
import shutil


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
        bin_dir = r'data/binary/' + filename
        backup_dir = r'data/backup/' + filename
        file_path = os.path.join(root_directory, bin_dir)
        backup_path = os.path.join(root_directory, backup_dir)
        try:
            print("Backing up " + filename + " to: " + backup_path)
            shutil.copy(file_path, backup_path)
        except:
            print('Error while back up')
        print("saving " + filename + " to: " + file_path)
        joblib.dump(model, file_path)
        print(filename + " saved to: " + file_path)
