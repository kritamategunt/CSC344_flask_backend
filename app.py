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
 
@app.route('/predict', methods = ['GET','POST'])
def prediction():
    if request.method == 'GET':
        return jsonify([{'res':'200 Ok ><','predict':predict,'x_value':x_value}])
    elif request.method == 'POST':
        input1 = request.json['input_x1']
        input2 = request.json['input_x2']
        input3 = request.json['input_x3']
        input4 = request.json['input_x4']
        input5 = request.json['input_x5']
        input6 = request.json['input_x6']
        input7 = request.json['input_x7']
        
        aws = int(input1)+1
        print(aws)
        return jsonify([{'ip' : int(input1)+int(input2)}])
        
 

if __name__ == '__main__':
    app.run(debug=True)
