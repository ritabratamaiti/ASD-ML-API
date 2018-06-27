
#RapidML created by Ritabrata Maiti
#Version: 1.0.0

import dill
import pandas as pd  
import os

def predictor():
 
    def fopen(str1, str2):
        dill_file = open(str1, str2)
        d = dill.load(dill_file)
        dill_file.close()
        return d

    df = fopen("df", "rb")
    f = fopen("f", "rb")
    model = fopen("model", "rb")
    dt = fopen("dt", "rb")   
    l = []
    i = 0
    for e in dt:
           
        l.append(e(f.split(',')[i]))     
        i+=1


    if(os.path.isfile('d')):
        d = fopen("d", "rb")      
        df.loc[0] = l
        fit = df.apply(lambda x: d[x.name].transform(x))
    else:
        fit = df
        
    df1 = fit.values
    X = df1[:, :(df1.shape[1]-1)]
    p = model.predict(X)
    if(os.path.isfile('d')):
            p = d[list(df)[-1]].inverse_transform(p)
    file = open('result.txt','w') 
    file.write(str(p[0]))
    file.close()
    return 0


    