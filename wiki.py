
import requests

class Wiki:
    """
    Wiki permet l'acquisition et le traitement des données de wikipedia
    """
    @staticmethod
    def wiki_story(ville):
        """
        méthode permettant d'acquérir les données Wikipédia
        """
        try:
            url_wiki =("https://fr.wikipedia.org/api/rest_v1/page/summary/" + ville)
            response = requests.get(url_wiki).json()
            return Wiki.wiki_data(response)
        except:
            url_wiki =("https://fr.wikipedia.org/api/rest_v1/page/summary/vire" )
            response = requests.get(url_wiki).json()
            return Wiki.wiki_data(response)
        
    @staticmethod
    def wiki_data(response):
        """
        methode permettant le traitement des données Wikipédia
        retourne :
        le titre de l'article : wiki_title
        le texte : wiki_text
        """

        if response['title'] == "Not found":
            wiki_data = {"wiki_title":"vire","wiki_text":"tu me prends pour une andouille .La demande me semble fantaisiste,pose moi une autre question"}
            return wiki_data

        else:
            wiki_title=(response['title'])
            wiki_text=(response['extract'])
            wiki_data={"wiki_title":wiki_title,"wiki_text":wiki_text}

            return wiki_data