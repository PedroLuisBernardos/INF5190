# __init__.py
from io import DEFAULT_BUFFER_SIZE
from flask import Flask, g
from config import Config
from flask_bootstrap import Bootstrap
from .database import Database
from app.errors import bp as errors_bp
from app.auth import bp as auth_bp
from app.rest import bp as rest_bp
from flask_json_schema import JsonSchema
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import csv
from os.path import exists
import xml.etree.ElementTree as ET
import re

app = Flask(__name__, static_url_path="", static_folder="static")
app.config.from_object(Config)
app.config['SECRET KEY'] = Config.SECRET_KEY
bootstrap = Bootstrap(app)
schema = JsonSchema(app)

# Retourne la base de données
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


# Deconnecte la base de donnees qui est connectee
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


# Telecharge les fichiers CSV et XML pour la base de donnees
# tous les jours a minuit
def telecharger():
    piscines = requests.get(Config.urlPiscines)
    patinoires = requests.get(Config.urlPatinoires)
    glissades = requests.get(Config.urlGlissades)
    open("app/static/piscines.csv", "wb").write(piscines.content)
    open("app/static/patinoires.xml", "wb").write(patinoires.content)
    open("app/static/glissades.xml", "wb").write(glissades.content)


# Cree les bases de donnees pour les piscines, les patinoires et les glissades
def create_piscine_db():
    with open('app/static/piscines.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)
        for row in reader:
            id_uev = row[0]
            style = row[1]
            nom = row[2]
            arrondisse = row[3]
            adresse = row[4]
            propriete = row[5]
            gestion = row[6]
            point_x = row[7]
            point_y = row[8]
            equipeme = row[9]
            longitude = row[10]
            latitude = row[11]

            # Verifier si la piscine existe deja, sinon la creer
            check_db = get_db().is_piscine(style, nom)
            if len(check_db) == 0:
                get_db().add_piscine(id_uev, style, nom, arrondisse,
                                     adresse, propriete, gestion,
                                     point_x, point_y, equipeme,
                                     longitude, latitude)
    csvfile.close()


def create_patinoire_db():
    with open('app/static/patinoires.xml', newline='') as xmlfile:
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        for i in range(len(root)):
            nom_arr = root[i][0].text.strip()
            for j in range(len(root[i][1])):
                if (root[i][1][j].tag == "nom_pat"):
                    nom_pat = root[i][1][0].text.strip()
                check_db = get_db().is_patinoire(nom_arr, nom_pat)
                if len(check_db) == 0:
                    get_db().add_patinoire(nom_arr, nom_pat)
                    #else:
                        #date_heure = root[i][1][j][0].text
                        #ouvert = root[i][1][j][1].text
                        #deblaye = root[i][1][j][2].text
                        #arrose = root[i][1][j][3].text
                        #resurface = root[i][1][j][4].text
                        #check_db = get_db().is_condition(date_heure, ouvert,
                        #                                 deblaye, arrose,
                        #                                 resurface, nom_pat)
                        #if len(check_db) == 0:
                        #    get_db().add_condition(date_heure, ouvert, deblaye,
                        #                           arrose, resurface, nom_pat)


def create_glissade_db():
    with open('app/static/glissades.xml', newline='') as xmlfile:
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        for i in range(len(root)):
            nom = root[i][0].text
            ouvert = root[i][2].text
            deblaye = root[i][3].text
            condition = root[i][4].text
            nom_arr = root[i][1][0].text
            cle = root[i][1][1].text
            date_maj = root[i][1][2].text
            check_db = get_db().is_arrondissement(nom_arr)
            if len(check_db) == 0:
                get_db().add_arrondissement(nom_arr, cle, date_maj)
            check_db = get_db().is_glissade(nom)
            if len(check_db) == 0:
                get_db().add_glissade(nom, ouvert, deblaye, condition, nom_arr)

# Creer la base de donnees
with app.app_context():
    if (exists("app/static/piscines.csv") and
        exists("app/static/patinoires.xml") and
            exists("app/static/glissades.xml")):
        schedule = BackgroundScheduler(daemon=True)
        schedule.add_job(telecharger, 'cron', day='*', hour='0')
        schedule.start()
        # TODO update bd apres un chanegemtn??
    else:
        telecharger()
        create_piscine_db()
        create_patinoire_db()
        create_glissade_db()

# Gestion des erreurs
app.register_blueprint(errors_bp)

# Gestion de l'authentification
app.register_blueprint(auth_bp)

# Gestion des requetes REST
app.register_blueprint(rest_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=true)

from app import views
