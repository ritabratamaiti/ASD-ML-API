# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 18:30:01 2018

@author: Ritabrata Maiti
"""

from flask import Flask, request
import dill
import helper


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
  return "Autism Detection API"


@app.route('/query', methods=['GET', 'POST'])
def query_example():
    req = request.args['ip']
    dill_file = open("f", "wb")
    dill_file.write(dill.dumps(req))
    dill_file.close()
    helper.predictor()
    file = open('result.txt','r') 
    res = file.read()
    file.close()
    return res

if __name__ == '__main__':
    app.run(debug=True, port=5000)

