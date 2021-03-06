# config.py
# Contient les variables de configuration de l'application
import os
import json


class Config(object):
    # YzNjbC0zNXQtYzRjaDM= est la cle secrete
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'YzNjbC0zNXQtYzRjaDM='

    # La liste des piscines et installations aquatiques en format CSV
    urlPiscines = ("https://data.montreal.ca/dataset/4604afb7-a7c4-4"
                   "626-a3ca-e136158133f2/resource/cbdca706-569e-4b4a"
                   "-805d-9af73af03b14/download/piscines.csv")

    # La liste des patinoires en format XML
    urlPatinoires = ("https://data.montreal.ca/dataset/225ac315-49fe-476"
                     "f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903"
                     "f-db24408bacd0/download/l29-patinoire.xml")

    # La liste des aires de jeux d'hiver (glissades) en format XML
    urlGlissades = ("http://www2.ville.montreal.qc.ca/services_citoyens/"
                    "pdf_transfert/L29_GLISSADE.xml")

    with open("schemas/create_glissades.json", "r") as f:
        schema_create_glissades = json.load(f)

    with open("schemas/create_patinoires.json", "r") as f:
        schema_create_patinoires = json.load(f)

    with open("schemas/create_piscines.json", "r") as f:
        schema_create_piscines = json.load(f)

    with open("schemas/update_glissades.json", "r") as f:
        schema_update_glissades = json.load(f)

    with open("schemas/update_patinoires.json", "r") as f:
        schema_update_patinoires = json.load(f)

    with open("schemas/update_piscines.json", "r") as f:
        schema_update_piscines = json.load(f)
