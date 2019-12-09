import pickle


class PredictionModel(object):
    def __init__(self, file_path, logger):
        self.logger = logger
        with open(file_path, 'rb') as file:
            self.model = pickle.load(file)

    def predict(self, samples):
        self.logger.debug('Predicting classes probabilities for samples: %s', samples)
        return self.model.predict_proba(samples)
