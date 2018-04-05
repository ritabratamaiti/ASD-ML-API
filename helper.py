# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:30:21 2018

@author: Ritabrata Maiti
"""
import dill
import pandas as pd  
from sklearn.externals import joblib

def predictor():
    clf = joblib.load('clf.pkl')
    
    def fopen(str1, str2):
        dill_file = open(str1, str2)
        d = dill.load(dill_file)
        dill_file.close()
        return d
    
    d = fopen("d", "rb")
    df = fopen("df", "rb")
    f = fopen("f", "rb")
    f = "0,"+f
    l = [int(e) if e.isdigit() else e for e in f.split(',')]
    df.loc[0] = l
    df.to_csv("out2.csv", sep=',')
    df = pd.read_csv('out2.csv')
    df = df.drop(['Unnamed: 0.1'], axis=1)
    df.iloc[:, 14:] = df.iloc[:, 14:].astype(str)
    fit = df.apply(lambda x: d[x.name].transform(x))
    df1 = fit.values
    X = df1[:, :(df1.shape[1]-1)]
    p = clf.predict(X)
    file = open('result.txt','w') 
    file.write(str(p[0]))
    file.close()
    return 0


