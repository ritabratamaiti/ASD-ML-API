# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 02:56:19 2018

@author: Ritabrata Maiti
@PROBLEM AREA: Autism Detection
@Dataset: Adult Autism Data
@Dataset URL: https://archive.ics.uci.edu/ml/datasets/Autism+Screening+Adult
"""
#df.apply(lambda x: d[x.name].transform(x))
#Use that in API

import pandas as pd   
from sklearn.naive_bayes import BernoulliNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from collections import defaultdict
d = defaultdict(LabelEncoder)
X = []
Y = []

df = pd.read_csv('newdata.csv', na_values = {'?'})
df = df.fillna("0") 
df.to_csv("out.csv", sep=',')
df = pd.read_csv('out.csv')
fit = df.apply(lambda x: d[x.name].fit_transform(x))
df = fit.values
X = df[:, :(df.shape[1]-1)]
Y = df[:, df.shape[1]-1]
clf = BernoulliNB()
clf.fit(X, Y)
kf = KFold(n_splits=10)
kf.get_n_splits(X)
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]
    print(clf.score(X_test, Y_test))  
    print(clf.score(X_train, Y_train))  
