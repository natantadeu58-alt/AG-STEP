from fastapi import APIRouter
from pydantic import BaseModel
from ai_detector import GatewayAnomalyDetector
router = APIRouter()
detector = GatewayAnomalyDetector()
dados_normais = [
    [45, 0], [50,0], [55, 1], [40, 0], [60, 0],
    [48, 1], [52, 0], [43, 0], [58, 0], [49, 1]
]
detector.train(dados_normais)
class TrafficData(BaseModel):
    packet_rate: float
    failed_auths: int 
@router.post("/analisar")
def analisar_trafego(data: TrafficData):
    amostra = [data.packet_rate, data.failed_auths]
    resultado = detector.predict(amostra)
    return {
        "status": "sucesso",
        "entrada": {"packet_rate": data.packet_rate, "failed_auths": data.failed_auths},
        "resultado_ia": resultado
    }