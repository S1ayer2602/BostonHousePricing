import pickle
from flask import Flask,request,app,jsonify,url_for,render_template,redirect,flash
import pandas as pd
import numpy as np

app = Flask(__name__)
## Load the model
model = pickle.load(open('regmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():