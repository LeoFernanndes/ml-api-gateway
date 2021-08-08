import joblib
import numpy as np


class IrisPredictorV1:
    def __init__(self):
        self.predictor = joblib.load("iris_predictor_v1.joblib")

    def predict(self, flower_data: list) -> str:
        flower_data_array = np.array(flower_data).reshape(1, -1)
        prediction = self.predictor.predict(flower_data_array)
        return prediction[0]
