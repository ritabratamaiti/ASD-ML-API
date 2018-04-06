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
from sklearn.externals import joblib
import dill


d = defaultdict(LabelEncoder)
X = []
Y = []

#Used initially to create out.csv

df = pd.read_csv('newdata.csv', na_values = {'?'})
df = df.fillna("0") 
df.to_csv("out.csv", sep=',')


#save a csv copy
df = pd.read_csv('out.csv')
df2 = df

#Labelencoding the table
fit = df.apply(lambda x: d[x.name].fit_transform(x))
df = fit.values

#gettin X and Y, for training the classifier
X = df[:, :(df.shape[1]-1)]
Y = df[:, df.shape[1]-1]

#Naive Bayes Classifier
clf = BernoulliNB()

#Testing Classifier using KFold splitting
kf = KFold(n_splits=10)
kf.get_n_splits(X)
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]
    clf.fit(X_test, Y_test)  
    print(clf.score(X_train, Y_train))  

#pickling the dictionary d
dill_file = open("d", "wb")
dill_file.write(dill.dumps(d))
dill_file.close()

#pickling the skeletal dataframe df_empty
df_empty = df2[0:0]
dill_file = open("df", "wb")
dill_file.write(dill.dumps(df_empty))
dill_file.close()

#retrainig and pickling the classifier
clf.fit(X, Y)
dill_file = open("clf", "wb")
dill_file.write(dill.dumps(clf))
dill_file.close()

dill_file = open("f", "wb")
dill_file.write(dill.dumps("0,0,0,0,0,0,0,1,0,1,2,30.0,m,White-European,no,no,Ireland,no,Self,NO"))
dill_file.close()