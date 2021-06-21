import requests
import os

class Geocoding:
    """
    Geocoding permet l'acquisition et le traitement des données Google
    """
    @staticmethod
    def data_geocoding(answer):
        """
        methode permettant d'acquerir les données Google
        """
        params = {
            'key': os.getenv("GOOGLE_API_KEY"),
            'address':answer
        }
        base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

        response = requests.get(base_url,params=params).json()
        return Geocoding.response_parsing(response)

    @staticmethod
    def response_parsing(response):
        """
        methode permettant le traitement des données Google
        retourne :
        l'adresse mise en forme :address_format
        les données gps:lat,lon
        le nom de la ville:ville
        """
        if response['status'] == 'OK':
            geometry = response['results'][0]['geometry']
            lat = geometry['location']['lat']
            lon = geometry['location']['lng']
            address_format=response['results'][0]['formatted_address']
            addresse_components = response['results'][0]['address_components']
            
            for elt in addresse_components:
                if (elt['types'][0]) == ('locality'):
                    ville = (elt['long_name'])

            données = (address_format,lat,lon,ville) 
            return données
        else:
            données = (None,0,0,"Truttemer-le-Grand")
            return données
           
    
