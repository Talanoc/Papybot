# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:01:21 2021
@author: 
"""

from flask import Flask, render_template,jsonify,request,url_for
from flask_cors import CORS
from stop_words_french import stop_words

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/question/<user_question>',methods=['get','post'])

def question(user_question):
  user_question_sw=[]

  user_question=user_question.split()

  user_question_sw=[element for element in user_question if element not in stop_words]

  return jsonify(user_question_sw)


app.run(debug=True)