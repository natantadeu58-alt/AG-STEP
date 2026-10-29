from fastapi import FastAPI
from routers import router
from pydantic import BaseModel
from ai_detector import GatewayAnomalyDetector
app = FastAPI(title="AG-STEP: Gateway Security & AI Platform")
app.include_router(router)
detector = GatewayAnomalyDetector()
class TrafficData(BaseModel):
    packet_rate: float
    failed_auths: int
@app.on_event("startup")
def startup_event():
    dados_normais = [
        [45, 0], [50, 0], [55,1], [40, 0], [60, 0],
        [48, 1], [52,0], [43, 0], [58, 0], [49, 1]
    ]
    detector.train(dados_normais)
    @app.get("/")
    def home():
        return {
            "status": "Online",
            "projeto": "AG-STEP Purple Team",
            "endpoints_disponiveis": ["/analisar", "/docs"]
        }
        @app.post("/analisar")
        def analisar_trafego(data: TrafficData):
            amostra = [data.packet_rate, data.failed_auths]
            resultado = detector.predict(amostra)
            return resultado 