from fastapi import FastAPI
from pydantic import BaseModel
from Model.model import predict_pipeline
from Model.model import __version__ as Modelversion



app = FastAPI()

class TextInput(BaseModel):
    text:str

class PredictionOutput(BaseModel):
    techniquePredicted: str



@app.get("/")
def home():
    return {"health_check": "OK", "model_version": Modelversion}

@app.post("/predict", response_model = PredictionOutput)
def predict(technique:TextInput):
    techPredicted= predict_pipeline(technique.text)
    return {"technique" : techPredicted}
