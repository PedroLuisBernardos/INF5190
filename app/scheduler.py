import requests
import csv
from app import Config, get_db
import xml.etree.ElementTree as ET
from os.path import exists
from apscheduler.schedulers.background import BackgroundScheduler


class SetUp:
    # Telecharge les fichiers CSV et XML pour la base de donnees
    # tous les jours a minuit
    def telecharger():
        piscines = requests.get(Config.urlPiscines)
        patinoires = requests.get(Config.urlPatinoires)
        glissades = requests.get(Config.urlGlissades)
        open("app/static/piscines.csv", "wb").write(piscines.content)
        open("app/static/patinoires.xml", "wb").write(patinoires.content)
        open("app/static/glissades.xml", "wb").write(glissades.content)

    # Cree les bases de donnees pour les piscines
    # les patinoires et les glissades
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
                    # else:
                        # date_heure = root[i][1][j][0].text
                        # ouvert = root[i][1][j][1].text
                        # deblaye = root[i][1][j][2].text
                        # arrose = root[i][1][j][3].text
                        # resurface = root[i][1][j][4].text
                        # check_db = get_db().is_condition(date_heure, ouvert,
                        #                                 deblaye, arrose,
                        #                                 resurface, nom_pat)
                        # if len(check_db) == 0:
                        #    get_db().add_condition(date_heure, ouvert,
                        #                           deblaye, arrose,
                        #                           resurface, nom_pat)

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
                    get_db().add_glissade(nom, ouvert, deblaye,
                                          condition, nom_arr)

    def run():
        # Creer la base de donnees
        if (exists("app/static/piscines.csv") and
            exists("app/static/patinoires.xml") and
                exists("app/static/glissades.xml") and
                exists("db/database.db")):
            schedule = BackgroundScheduler(daemon=True)
            schedule.add_job(SetUp().telecharger, 'cron', day='*', hour='0')
            schedule.start()
        else:
            SetUp.telecharger()
            SetUp.create_piscine_db()
            SetUp.create_patinoire_db()
            SetUp.create_glissade_db()
