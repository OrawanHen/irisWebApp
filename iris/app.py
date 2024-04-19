# app.py

from flask import Flask, render_template, request, jsonify
from iris_model import predict_iris

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/forcast', methods=['POST'])
def predict():
    sep_length = float(request.form['Sepallength'])
    sep_width = float(request.form['Sepalwidth'])
    pet_length = float(request.form['Petallength'])
    pet_width = float(request.form['Petalwidth'])
    result = predict_iris(sep_length, sep_width, pet_length, pet_width)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
