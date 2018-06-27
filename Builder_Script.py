
# coding: utf-8

# In[1]:


import RapidML
import os
import pandas as pd


# This Autism Screening Adult Data Set is from UCI Machine Learning Repository and is available here: https://archive.ics.uci.edu/ml/datasets/Autism+Screening+Adult

# In[2]:


df = pd.read_csv('out.csv')
df = df.drop(columns = ['Unnamed: 0'])
df.head()


# In[4]:


mod = RapidML.rapid_classifier(df,name='ASDapi')

