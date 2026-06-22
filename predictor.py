"Model loading and prediction logic."

import pickle
import pandas as pd
from config import features, risk_bands, model_path, scaler_path


class FWIPredictor:
    """Wraps the trained model and scaler, and handles prediction + risk lookup."""

    def __init__(self, model_path=model_path, scaler_path=scaler_path):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        with open(scaler_path, 'rb') as f:
            self.scaler = pickle.load(f)

    def predict(self, values: dict) -> float:
        """Takes a dict of {feature_name: value} and returns the predicted FWI."""
        row = pd.DataFrame([[values[f] for f in features]], columns=features)
        scaled = self.scaler.transform(row)
        fwi = float(self.model.predict(scaled)[0])
        return max(0.0, round(fwi, 2))

    @staticmethod
    def risk_for(fwi: float) -> dict:
        """Looks up the risk band for a given FWI value."""
        for band in risk_bands:
            if fwi <= band['max']:
                return band
        return risk_bands[-1]