# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 00:48:22 2023

@author: Prajwal Arjun Sonkavde
"""
from flask import Flask , request , render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("breastcancer/rf.pkl", "rb"))
print("Model Loaded")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['name']
    age = request.form['age']
    race = request.form['race']
    marital_status = request.form['marital_status']
    tstage = request.form['t-stage']
    nstage = request.form['n-stage']
    th6stage = request.form['6th-stage']
    grade = request.form['grade']
    a_stage = request.form['a_stage']
    tumor_size = request.form['tumor_size']
    estrogen_status = request.form['estrogen_status']
    progesterone_status = request.form['progesterone_status']
    regional_node_examined = request.form['regional_node_examined']
    regional_node_positive = request.form['regional_node_positive']
    survived_months = request.form['survived_months']


    prediction = model.predict([[age,race ,marital_status ,tstage ,nstage,th6stage ,grade,a_stage ,tumor_size ,estrogen_status,progesterone_status,regional_node_examined ,regional_node_positive ,survived_months]])
  
    if prediction == 1 :
        prediction = "{} your free of cancer".format(name)
    else:
        prediction="{} , Get Treatment as soon as possible , there is a probability that you have cancer".format(name)
        
        
    return render_template("prediction.html",pred=prediction)

if __name__=='__main__':
    app.run(debug=True)