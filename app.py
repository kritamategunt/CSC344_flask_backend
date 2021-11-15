from typing import Sized
from flask import Flask, render_template, url_for, jsonify, request
import io
import string
import time
import os
import numpy as np
import pickle
import numpy as np
# import requests
import json
# from sklearn.externals import joblib
from model import reg

app = Flask(__name__)

post = [
    {
        'author': 'Kritamate Kamheang',
        'title': 'post 1',
        'content': 'First test',
        'date': 'jun 4,2021'
    },
    {
        'author': 'Matetaki gnaehmak',
        'title': 'post 2',
        'content': 'second test',
        'date': 'april 6,2021'
    },
]

# joblib.dump(mymodel, "linear_regression_model.pkl")


@app.route("/")
@app.route("/home")
def home():
    return render_template('homepage.html', posts=post,)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


# @app.route('/predict', methods=['GET', 'POST'])
# def prediction():
#     if request.method == 'GET':
#         return jsonify([{'res': '200 Ok ><', 'predict': predict, 'x_value': x_value}])
#     elif request.method == 'POST':
#         input_x = np.zeros(7)
#         for i in input_x:
#             x = request.form.get('x')
#             input_x.append(x)
#             break

#         return jsonify([{'ip': input_x}])


# allow both GET and POST requests

@app.route('/predict', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        inputX = request.form.get('x')
        inputY = request.form['y']
        inputX_predict = request.form['x_predict']
        ary_x = []
        ary_y = []
        tempX = ''
        tempY = ''
        inputX += ','
        inputY += ','

        for i in range(len(inputX)):
            if inputX[i] != ",":
                tempX = tempX+inputX[i]

            else:
                #int(tempX)
                ary_x.append(tempX)
                tempX = ''

        for i in range(len(inputY)):
            if inputY[i] != ",":
                tempY = tempY+inputY[i]

            else:
                #int(tempY)
                ary_y.append(tempY)
                tempY = ''
        for i in range(len(ary_x)):
            ary_x[i]=(float(ary_x[i]))
            # print(ary_x[i])
            # print(type(ary_x[i]))

        for i in range(len(ary_y)):
            ary_y[i]=(float(ary_y[i]))
            # print(ary_y[i])
            # print(type(ary_y[i]))
        
        # print(ary_x)
        # print(ary_y)
        # print(inputX_predict)
        #ans = reg(ary_x,ary_y,inputX_predict)
        #print(ans)
        # print('--MOCK INPUT--')
        # print(reg([1,2,3],[1,2,3],4))

        print('REAL INPUT')
        #print(reg(ary_x,ary_y,7))
        ans=reg(ary_x,ary_y,float(inputX_predict))


    
        return jsonify({'x': ary_x, 'y': ary_y, "inputX_predict": inputX_predict,"ans":ans})
        #return ary_x,ary_y

    elif request.method == "GET":
        return jsonify({'status ': 200, 'predict': 'model.reg', 'x_value': 'model.x_value'})



# def resg(ary_x,ary_y,inputX_predict):
#     x = ary_x
#     y= ary_y
#     for i in range(30):

#         mymodel_i = numpy.poly1d(numpy.polyfit(x, y, i+1))
#         nextScore = r2_score(y, mymodel_i(x))

#         mymodel = numpy.poly1d(numpy.polyfit(x, y, i))
#         pevScore = r2_score(y, mymodel(x))
  

#         if pevScore < nextScore:
#             nextScore = pevScore
#         elif nextScore <= pevScore:
#             break

#     x_value = inputX_predict
#     predict = mymodel(x_value)
#     return mymodel(x_value)
   


@app.route('/getlist')
def status():
    first_status = request.args.get("status")
    statuses = request.args.getlist("status")
    return "First Status: '{}'\nAll Statuses: '{}'".format(first_status, statuses)


if __name__ == '__main__':
    app.run(debug=True)
    