# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:01:21 2021

@author: 33633
"""

from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/test')
def test():
  return "toto"


app.run(debug=True)