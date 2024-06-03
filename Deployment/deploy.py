from flask import Flask, render_template, request
import joblib

from constante import MODEL_PATH, VECTORIZER_PATH, FILE_PATH

app= Flask(__name__)

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template(FILE_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['inputText']
    print(input_text)
    text = [input_text]
    X = vectorizer.transform(text)
    predictions = model.predict(X)[0]
    
    return render_template(FILE_PATH, prediction=predictions)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='80')