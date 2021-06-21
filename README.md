# Papybot - Projet 7

## I. Description

Ce programme a pour but de créer un bot capable de répondre à une question d'un utilisateur.
L'application est basée sur l'API Wikipedia et de l'API Google.
Cette application permet d'afficher une adresse, une carte et des informations générales sur cette ville.

## II. Hébergement de l'application

Adresse de l'application : `https://talanoc-papybot.herokuapp.com/`.

## III. Fonctionnement de l'application

-lancement de l'application.
-entrée d'une demande ("je cherche une boulangerie à rouen" par exemple)
-click de l'utilisateur sur "lancer la rechedrche".
-élimination des stops-words de la question pour obtenir une demande simplifiée (user_question_sw).
-passage de user_question_sw dans l'API Googlemaps.Nous obtenons de l'api les données suivantes :address_format , lat , lon , ville.
-passage de la donnée ville dans l'API Wikipedia pour obtenir une description succinte de la ville.
-affichage de la réponse dans la page html.

## IV. Requirements

-Python 3.9.5
-Flask
-Flask-cors
-Requests
-Gunicorn

-Api Google-maps (GOOGLE_API_KEY doit être intégrée dans les variables d'environnements windows )
-Api Wikipedia
-Api Fetch
