from flask import Flask, render_template, request

import pandas as pd
import joblib

app= Flask(__name__)

model = joblib.load(r'G:\NLP Projects\MitRA aTTACK\Notre projet\Models\ML Models\SVC.pkl')

vectorizer = joblib.load(r'G:\NLP Projects\MitRA aTTACK\Notre projet\Models\ML Models\vectorizer.joblib')
    
FILE_PATH= 'index.html'

@app.route('/', methods=['GET'])
def hello_world():
    return render_template(FILE_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['inputText']
    print(input_text)
    text = [inputText]
    X = vectorizer.transform(text)
    predictions = model.predict(X)
    
    return render_template(FILE_PATH, prediction="hello world")    

if __name__ == "__main__":
    app.run(port=80, debug=False)