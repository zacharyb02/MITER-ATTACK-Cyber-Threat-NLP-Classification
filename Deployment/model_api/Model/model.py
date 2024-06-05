import joblib
from pathlib import Path

__version__= "0.1.0"

BASE_DIR = Path(__name__).resolve().parent
MODEL_PATH =f'{BASE_DIR}/Model/SVC-{__version__}.pkl'
VECTORIZER_PATH =f'{BASE_DIR}/Model/vectorizer-{__version__}.joblib'


model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def predict_pipeline(text):
    X = vectorizer.transform(text)
    predictions = model.predict(X)[0]
    return predictions

