import pickle
import os


class PersistenceUtils:
    def __init__(self):
        pass

    @staticmethod
    def write_pickle(file_path, data):
        with open(file_path, "wb") as f:
            pickle.dump(data, f)

    @staticmethod
    def load_pickle(file_path):
        with open(file_path, "rb") as f:
            data = pickle.load(f)
        return data
