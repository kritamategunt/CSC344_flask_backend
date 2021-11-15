import matplotlib.pyplot as plt
from scipy import stats
import numpy
from sklearn.metrics import r2_score
#import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
#import requests
import json




  

  

def reg(Xin,Yin,x_predict):
  x = Xin
  #X as a time serie (in each day)
  y = Yin
  #y as a selling number from input in our application
  x_value = x_predict
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
  x_value = x_predict
  predict = mymodel(x_value)
  print('x value equal to ',x_value)
  print('Prediction: ',predict)
  #plt.scatter(x, y)
  myline = numpy.linspace(1, 22, 100)
  #plt.plot(myline, mymodel(myline))
  #plt.show()

  return(predict)


x1 = [1,2,3,4,5,6]
y1= [1,2,3,4,5,6]
x2 = 7
reg(x1,y1,x2)
