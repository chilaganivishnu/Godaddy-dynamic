from flask import Flask, render_template, request
import requests
import numpy as np
app=Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    return render_template('diabetes.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        pregnancies=int(request.form['Pregnancies'])
        age=int(request.form['age'])
    return render_template('diabetes.html',text="hello")

if __name__=="__main__":
    app.run(debug=True)