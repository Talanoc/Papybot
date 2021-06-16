
from flask import Flask,render_template,jsonify
from flask_cors import CORS
from traitement_question import Question
from geocoding import Geocoding
from wiki import Wiki

app = Flask(__name__)
CORS(app)


@app.route('/')
def index(): 
  return render_template('index.html')

@app.route('/question/<user_question>',methods=['get'])
def question(user_question):
  answer=Question.traitement_question(user_question)
  geo=Geocoding.data_geocoding(answer)
  ville=(geo[3])
  wiki=Wiki.wiki_story(ville) 
  return jsonify({"status":"OK" if geo else "error","address":geo[0] if geo else None,"lon":geo[2] if geo else None,"lat":geo[1] if geo else None,"wiki":wiki,"user_question_sw":answer})

if __name__=='__main__':
    app.run(debug=False)

