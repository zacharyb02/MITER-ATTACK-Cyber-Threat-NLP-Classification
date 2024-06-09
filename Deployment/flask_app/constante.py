from pathlib import Path

BASE_DIR = Path(__name__).resolve().parent
MODEL_PATH = BASE_DIR / r'Model/SVC.pkl'
VECTORIZER_PATH = BASE_DIR / r'Model/vectorizer.joblib'
MAIN_PATH = 'index.html'
ABOUT_PATH = 'about.html'
FASTAPI_URL = "http://127.0.0.1:8000/predict" 