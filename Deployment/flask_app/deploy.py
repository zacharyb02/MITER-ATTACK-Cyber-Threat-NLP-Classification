from flask import Flask, render_template, request
import requests
from pymongo import MongoClient
from dotenv import load_dotenv

import os
import re

load_dotenv()

from constante import MAIN_PATH, ABOUT_PATH, FASTAPI_URL

def remove_indices(text):
    
    return re.sub(r'\[\d+\]', '', text)

mongodb_user = os.getenv('MONGODB_USER')
mongodb_password = os.getenv('MONGODB_PASSWORD')


app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(f'mongodb://{mongodb_user}:{mongodb_password}@localhost:27017/')
db = client['tactic']


def find_technique_by_id(technique_id):
    technique = db.technique.find_one({"technique-ID": technique_id})
    return technique



@app.route('/', methods=['GET'])
def main_page():
    return render_template(MAIN_PATH)

@app.route('/about', methods=['GET'])
def about_page():
    return render_template(ABOUT_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['inputText']
    print(input_text)
    data = {
        "text": input_text
    }
    response = requests.post(FASTAPI_URL, json=data)
    prediction = response.json().get('techniquePredicted')

    # Search in MongoDB for the tactic with the given ID
    tactic = db.technique.find_one({"technique-ID": prediction})
    
    

    tactic_info = tactic.get('technique-description', 'No description available')
    tactic_name = tactic.get('technique-name', 'No description available')
    
        
    print(tactic_info)
    return render_template(MAIN_PATH, prediction=prediction, tactic_info=[remove_indices(paragraphe) for paragraphe in tactic_info], tactic_name = tactic_name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='80')
