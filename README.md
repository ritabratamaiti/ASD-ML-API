# Autism detection API
Hi!

I am Ritabrata Maiti, the creator of the Autism Detection API. Find me on LinkedIn here: linkedin.com/in/ritabratamaiti/

ASD refers to Autism Spectrum Disorder

## This project has 3 goals:
1. To find out the best machine learning pipeline for predicting ASD cases using genetic algorithms, via the TPOT library. (Classification Problem)
2. Compare the accuracy of the accuracy of the determined pipeline, with a standard Naive-Bayes classifier.
3. Saving the classifier as an external file, and use this file in a Flask API to make predictions in the cloud.

The first 2 goals are achieved via the [builder.py](../Autism-Detection-API/builder.py) script, which cleans the datasets, performs label encoding and finds the best-fitted classifier pipeline using genetic algorithms from the TPOT library. Furthermore, the builder script produces the files d, df, clf, and f. 
* d: This file contains the pickled dictionary used to label-encode the database.
* df: The file contains the pickled skeletal dictionary of the original database.
* clf: This file contains the pickled classifier pipeline that has the highest accuracy, determined via genetic algorithms.
* f: This file contains a dummy row, as initial input that is later utilized by the API script.

The final goal, implementing the flask API, is achieved by the [helper](../Autism-Detection-API/helper.py) and [API](../Autism-Detection-API/API.py) scripts. The helper script reads the files created by the builder and uses the saved models to predict an output, from the input obtained from the API request. The API script handles the actual requests and calls the helper script to predict and return an output.

## In order to build the project on your own, you require:
* [A Python 3.6 installation](https://www.python.org/downloads/)
* [The latest scikit learn installation](http://scikit-learn.org/stable/install.html)
* [The latest TPOT installation](https://epistasislab.github.io/tpot/installing/)
* [The latest Flask installation](http://flask.pocoo.org/docs/1.0/installation/#)
* [The dill Python library](https://pypi.org/project/dill/#description)

### Do note that you do not need to install flask if you plan on only deploying the project to the cloud, and don't plan on running it locally.

In order to deploy our flask app to the cloud, we use a service called pythonanywhere. At its free tier, it allows one python web app per account. 

In the files-tab create a new directory, and upload the files d, df, clf, f as well as the API and the helper scripts. Then create a new web application in the web apps tab and create a new virtualenv as well, and link it to the web app. My instructions are vague, and I highly recommend you check this [official guide](https://help.pythonanywhere.com/pages/Flask/) 

### Note: Before you deploy your web app, go to the directory: /home/"username"/.virtualenvs/"virtualenvname"/bin and delete the file: no-global-site-packages.txt 

This allows the web app to use external libraries outside the vitualenv, and proceeding without the above modifications causes a glitch/error.
