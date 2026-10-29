import numpy as np 
from sklearn.ensemble import IsolationForest
class GatewayAnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.is_trained = False
    def train(self, normal_data: list):
            X = np.array(normal_data)
            self.model.fit(X)
            self.is_trained = True
    def predict(self, sample: list) -> dict:
        print("--- A EXECUTAR O FICHEIRO:", __file__)
        if not self.is_trained:
            return {"error": "O modelo ainda não foi treinado."}
        X = np.array([sample])
        prediction = self.model.predict(X)[0]
        score = self.model.decision_function(X)[0]
        print("DEBUG - Prediction:", prediction)
        print("DEBUG - score:", score)
        resposta = {
            "is_anomaly": bool(prediction == -1),
            "anomaly_score": float(score)
        }
        print("DEBUG - Resposta a retornar:", resposta)
        return resposta