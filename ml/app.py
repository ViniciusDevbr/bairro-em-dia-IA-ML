import os, joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

MODEL_PATH = os.getenv("MODEL_PATH", "model/random_forest.joblib")
app = FastAPI(title="Bairro em Dia — Serviço de Machine Learning", version="1.0.0")
model = None
@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)

class PredictionInput(BaseModel):
    categoria: str
    regiao: str
    mes: int = Field(ge=1, le=12)
    dia_semana: int = Field(ge=1, le=7)
    canal: str = "MOBILE"

@app.get("/health")
def health():
    return {"status": "UP", "model_loaded": model is not None}

@app.post("/predict")
def predict(data: PredictionInput):
    if model is None:
        raise HTTPException(status_code=503, detail="Modelo não treinado. Execute o notebook e salve o artefato.")
    import pandas as pd
    frame = pd.DataFrame([data.model_dump()])
    try:
        probability = float(model.predict_proba(frame)[0][1])
    except Exception as exc:
        raise HTTPException(status_code=422, detail=f"Não foi possível processar as features: {exc}")
    return {"probabilidade_atraso": probability, "classe_prevista": int(probability >= 0.5),
            "aviso": "Estimativa estatística baseada nos dados históricos; não é garantia de prazo."}
