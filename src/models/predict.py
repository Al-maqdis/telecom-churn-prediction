"""
Prediction utilities.
"""

import joblib


class ChurnPredictor:

    def __init__(self, model_path):

        self.model = joblib.load(model_path)

    def predict(self, X):

        return self.model.predict(X)

    def predict_probability(self, X):

        return self.model.predict_proba(X)