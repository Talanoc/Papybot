from geocoding import Geocoding
from traitement_question import Question
import json
from wiki import Wiki

user_question='je cherche une boulangerie à vire'


def test_traitement_question():
    assert Question.traitement_question(user_question) == ('boulangerie à vire','je cherche une boulangerie à vire')

def test_response_parsing():
    mock_geocoding = 'mock_geocoding.json'   
    with open(mock_geocoding) as json_file:
        response = json.load(json_file)
    assert Geocoding.response_parsing(response) == ('1 Rue Georges Fauvel, 14500 Vire, France', 48.8391659, -0.8820916999999999, 'Vire')
 
def test_wiki_story():
    mock_wiki='mock_wiki.json'
    with open(mock_wiki) as json_file:
        response=json.load(json_file)
        
    assert Wiki.wiki_data(response)== {'wiki_title': 'Naveil', 'wiki_text': 'Naveil est une commune franÃ§aise situÃ©e dans le dÃ©partement de Loir-et-Cher, en rÃ©gion Centre-Val de Loire.'}
