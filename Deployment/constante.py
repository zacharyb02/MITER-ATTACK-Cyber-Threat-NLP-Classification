from pathlib import Path

BASE_DIR = Path(__name__).resolve().parent
MODEL_PATH = BASE_DIR / r'Model/SVC.pkl'
VECTORIZER_PATH = BASE_DIR / r'Model/vectorizer.joblib'
FILE_PATH= 'index.html'