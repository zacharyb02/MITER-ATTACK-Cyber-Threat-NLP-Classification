from flask import Flask, render_template, request
import requests


from constante import MAIN_PATH, ABOUT_PATH, FASTAPI_URL

app = Flask(__name__)



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

    return render_template(MAIN_PATH, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='80')
