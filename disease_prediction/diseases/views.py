from django.shortcuts import render
import numpy as np 
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
from sklearn.ensemble import ExtraTreesClassifier


def heart(request):
    return render(request, 'diseases/heart.html')


def liver(request):
    return render(request, 'diseases/liver.html')


def kidney(request):
    return render(request, 'diseases/kidney.html')


def diabetes(request):
    return render(request, 'diseases/diabetes.html')


def breastCancer(request):
    return render(request, 'diseases/breastCancer.html')

def result(request):
    data = pd.read_csv(r'C:\Users\Lenovo\Downloads\BTP\diabetes.csv')

    x=data.drop('Outcome', axis=1)
    y=data['Outcome']
    xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=.40, random_state=1)
    scaler = StandardScaler()
    xtrain = scaler.fit_transform(xtrain)
    xtest = scaler.transform(xtest)
    log = LogisticRegression()
    log.fit(xtrain,ytrain)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred = log.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    
    # // 0 indicates that person has diabetes_result
    result1 = ""
    if(pred != [1]):
        result1 = "Negative"
    else:
        result1 = "Positive"
    
    return render(request, 'diseases/diabetes.html', {"result2" : result1})


