
#RD_AML created by Ritabrata Maiti
#Version: 1.0.0

from flask import Flask, request
import dill
import helper
import numpy as np

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
  return "RapidMLex, Project Version: 1.0.0"


@app.route('/query', methods=['GET', 'POST'])
def query_example():
    req = request.args['ip']
    dill_file = open("f", "rb")
    f = dill.load(dill_file)
    dill_file.close()
    dill_file = open("dt", "rb")
    dt = dill.load(dill_file)
    dill_file.close()
    l = []
    i=0
    for e in f.split(','):
           k = dt[i]
           l.append(k(e))
           i+=1
    req = req + ',' + l[-1]
    dill_file = open("f", "wb")
    dill_file.write(dill.dumps(req))
    dill_file.close()
    helper.predictor()
    file = open('result.txt','r') 
    res = file.read()
    file.close()
    return res


if __name__ == '__main__':
    app.run(debug=True, port=8080)
