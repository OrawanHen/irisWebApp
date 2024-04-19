# app.py

from flask import Flask, render_template, request, jsonify
from insertIris import insert_data
from iris_model import predict_iris
from alldata import fetch_data_from_database


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
    result_message, iris_type = predict_iris(sep_length, sep_width, pet_length, pet_width)    
    insert_data("{:.2f}".format(sep_length), "{:.2f}".format(sep_width), "{:.2f}".format(pet_length), "{:.2f}".format(pet_width), iris_type)    
    return render_template('index.html', result=result_message)

@app.route('/All_result', methods=['GET','POST'])
def allresult():
    alldata = fetch_data_from_database()
    return render_template('All_result.html', alldata=alldata)


if __name__ == '__main__':
    app.run(debug=True)
