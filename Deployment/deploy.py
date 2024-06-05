from flask import Flask, render_template, request
import joblib

from constante import MODEL_PATH, VECTORIZER_PATH, MAIN_PATH, ABOUT_PATH

app= Flask(__name__)

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

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
    text = [input_text]
    X = vectorizer.transform(text)
    predictions = model.predict(X)[0]
    
    return render_template(MAIN_PATH, prediction=predictions)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port='80')