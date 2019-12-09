import pickle


class PredictionModel(object):
    def __init__(self, file_path):
        with open(file_path, 'rb') as file:
            self.model = pickle.load(file)

    def predict(self, features):
        return self.model.predict_proba(features)
