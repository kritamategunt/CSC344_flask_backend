from flask import Flask, render_template, url_for, jsonify, request
import io
import string
import time
import os
import numpy as np
import pickle
import numpy as np
# from sklearn.externals import joblib
from model import predict,x_value

app = Flask(__name__)

post = [
    {
        'author': 'Kritamate Kamheang',
        'title': 'post 1',
        'content': 'First test',
        'date' : 'jun 4,2021'
    },
    {
        'author': 'Matetaki gnaehmak',
        'title': 'post 2',
        'content': 'second test',
        'date' : 'april 6,2021'
    },
]

# joblib.dump(mymodel, "linear_regression_model.pkl")


@app.route("/")

@app.route("/home")
def home():
    return render_template('homepage.html',posts = post,)

@app.route("/about")
def about():
    return render_template('about.html',title = 'About' )
 
@app.route('/prediction', methods = ['GET','POST'])
def prediction():
    if request.method == 'GET':
        return jsonify({'res':'200 Ok ><'},{'predict':predict},{'x_value':x_value})
    elif request.method == 'POST':
        req_Json = request.json
        input = req_Json['input_x']
        return jsonify({'res': 'value_x, ' + input})
        
# @app.route("/predict", methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         try:
#             data = request.get_json()
#             years_of_experience = float(data["yearsOfExperience"])
            
#             lin_reg = joblib.load("./linear_regression_model.pkl")
#         except ValueError:
#             return jsonify("Please enter a number.")

#         return jsonify(lin_reg.predict(years_of_experience).tolist())


if __name__ == '__main__':
    app.run(debug=True)
