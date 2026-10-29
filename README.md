# **AG-STEP**

Monitoramento e segurança de redes baseados em inteligência artificial. O AG-STEP é uma API assíncrona, construída com FastAPI, que recebe métricas de tráfego de rede e usa um modelo de Machine Learning (Isolation Forest, do scikit-learn) para identificar comportamentos anômalos.

---

## **Funcionalidades**

* **API assíncrona com FastAPI:** recebe pedidos HTTP com métricas de rede, como taxa de pacotes e tentativas de autenticação falhadas, e devolve o resultado da análise em JSON.
* **Detecção de anomalias com Isolation Forest:** o modelo aprende o que é tráfego "normal" a partir de dados padrão e, para cada novo conjunto de métricas, indica se ele é seguro ou uma possível ameaça.
* **Pontuação de risco:** cada análise devolve `is_anomaly` (anomalia ou não) e `anomaly_score` (nível de desvio em relação ao comportamento normal).
* **Cliente de teste:** o script `test_api.py` envia métricas de exemplo à API para validar o funcionamento.

---

## **Tecnologias utilizadas**

* Python 3.x
* FastAPI (API assíncrona)
* Uvicorn (servidor da aplicação)
* scikit-learn (algoritmo Isolation Forest)
* NumPy (processamento dos dados de entrada)

---

## **Componentes principais**

| Componente | Arquivo | Função |
|---|---|---|
| Servidor da API | `app = FastAPI()` | Instância principal da aplicação. Gerencia as rotas e recebe os pedidos HTTP externos. |
| Rotas | `routers.py` | Recebe os dados enviados pelo cliente e os encaminha para o detector de IA. |
| Detector de anomalias | `ai_detector.py` | Contém o modelo Isolation Forest. O método `train` aprende o comportamento normal, e o método `predict` avalia novos dados. |
| Inicialização | `run.py` | Inicia o Uvicorn e deixa a aplicação à escuta de pedidos. |
| Cliente de teste | `test_api.py` | Envia métricas de rede de exemplo para a API. |
| Dependências | `requirements.txt` | Lista as bibliotecas necessárias (FastAPI, Uvicorn, scikit-learn e NumPy). |

---

## **Como funciona**

1. **Inicialização:** o `run.py` sobe o servidor com Uvicorn, e a aplicação FastAPI fica à escuta na porta configurada.
2. **Envio de dados:** um cliente, como o `test_api.py`, envia um conjunto de métricas de rede em um pedido HTTP.
3. **Processamento:** a rota em `routers.py` recebe os dados e os encaminha para a classe de detecção.
4. **Previsão:** o método `predict` converte os dados em um array NumPy, aplica o modelo Isolation Forest e avalia o desvio em relação ao comportamento normal.
5. **Resposta:** a API devolve um JSON com o resultado da análise (`resultado_ia`), indicando se há anomalia (`is_anomaly`) e o nível de risco (`anomaly_score`).

Exemplo ilustrativo de resposta (ajuste ao formato real da sua saída):

```json
{
  "resultado_ia": {
    "is_anomaly": true,
    "anomaly_score": 0.0
  }
}
```

---

## **Como usar**

```bash
pip install -r requirements.txt

python run.py
```

Com a API rodando, a documentação interativa fica disponível em `http://127.0.0.1:[porta]/docs`, onde é possível testar os endpoints pelo navegador.

Em outro terminal, execute o cliente de teste:

```bash
python test_api.py
```

---

## **Aviso**

Projeto desenvolvido para fins educacionais. Monitore apenas redes e dispositivos que você tem autorização para analisar.

---

## **Autor**

**Natan Tadeu dos Santos Coelho**
Estudante de Engenharia de Software e Cybersecurity | Futuro Engenheiro de Segurança Cibernética
