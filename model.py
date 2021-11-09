import matplotlib.pyplot as plt
from scipy import stats
import numpy
from sklearn.metrics import r2_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
#import requests
import json

x = [1,2,3,4,5,6,7]
y = [1,2,3,4,5,6,7]

#x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22] 
#X as a time serie (in each day)
#y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
#y as a selling number from input in our application

for i in range(30):

  mymodel_i = numpy.poly1d(numpy.polyfit(x, y, i+1))
  nextScore = r2_score(y, mymodel_i(x))

  mymodel = numpy.poly1d(numpy.polyfit(x, y, i))
  pevScore = r2_score(y, mymodel(x))
  
  #print('round,',i)
  if pevScore < nextScore:
    nextScore = pevScore
  elif nextScore <= pevScore:
    break
  

# print('r value ',r2_score(y, mymodel_i(x)))
x_value = 9
predict = mymodel(x_value)
# print('x value equal to ',x_value)
# print('Prediction: ',predict)
# plt.scatter(x, y)
myline = numpy.linspace(1, 22, 100)
# plt.plot(myline, mymodel(myline))
# plt.show()