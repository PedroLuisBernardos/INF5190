# database.py
# Defini les fonctions en lien avec la base de donnees
import sqlite3
import json
import collections
from sqlite3.dbapi2 import Cursor, connect


class Database:
    def __init__(self):
        self.connection = None

    # Fait une connection avec la base de donnees
    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/database.db')
        return self.connection

    # Deconnecte la base de donnees connectee
    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    # Recherche si une piscine existe selon la cle primaire
    def is_piscine(self, style, nom):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM piscine WHERE \
                       style=? and nom=?", (style, nom))
        return cursor.fetchall()

    # Cree une piscine
    def add_piscine(self, id_uev, style, nom, arrondisse, adresse, propriete,
                    gestion, point_x, point_y, equipeme, longitude, latitude):
        connect = self.get_connection()
        cursor = connect.cursor()
        try:
            cursor.execute(("INSERT INTO piscine(id_uev, style, nom, \
                            arrondisse, adresse, propriete, gestion, point_x, \
                            point_y, equipeme, longitude, latitude)"
                        "values(?,?,?,?,?,?,?,?,?,?,?,?)"),
                        (id_uev, style, nom, arrondisse, adresse, propriete,
                        gestion, point_x, point_y, equipeme,
                        longitude, latitude))
            connect.commit()
        except:
            connect.rollback()
            

    # Recherche si une glissade existe selon la cle primaire
    def is_glissade(self, nom):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM glissade WHERE nom=?", (nom,))
        return cursor.fetchall()

    # Cree une glissade
    def add_glissade(self, nom, ouvert, deblaye, condition, nom_arr):
        connect = self.get_connection()
        cursor = connect.cursor()
        try:
            cursor.execute(("INSERT INTO glissade(nom, ouvert, deblaye, \
                            condition, nom_arr)" "values(?,?,?,?,?)"),
                           (nom, ouvert, deblaye, condition, nom_arr))
            connect.commit()
        except:
            connect.rollback()


    # Recherche si une glissade existe selon la cle primaire
    def is_arrondissement(self, nom_arr):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM arrondissement WHERE nom_arr=?",
                       (nom_arr,))
        return cursor.fetchall()

    # Cree un arrondissement
    def add_arrondissement(self, nom_arr, cle, date_maj):
        connect = self.get_connection()
        cursor = connect.cursor()
        try:
            cursor.execute(("INSERT INTO arrondissement(nom_arr, cle, date_maj)"
                            "values(?,?,?)"), (nom_arr, cle, date_maj))
            connect.commit()
        except:
            connect.rollback()

    # Recherche si une patinoire existe selon la cle primaire
    def is_patinoire(self, nom_arr, nom_pat):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM patinoire WHERE \
                       nom_arr=? and nom_pat=?", (nom_arr, nom_pat))
        return cursor.fetchall()

    # Cree une patinoire
    def add_patinoire(self, nom_arr, nom_pat):
        connect = self.get_connection()
        cursor = connect.cursor()
        try:
            cursor.execute(("INSERT INTO patinoire(nom_arr, nom_pat)"
                            "values(?,?)"), (nom_arr, nom_pat))
            connect.commit()
        except:
            connect.rollback()

    # Recherche si une condition existe
    def is_condition(self, date_heure, ouvert, deblaye, arrose, resurface,
                     nom_pat):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM condition WHERE \
                       date_heure=? and ouvert=? and deblaye=? and\
                       arrose=? and resurface=? and nom_pat=?",
                       (date_heure, ouvert, deblaye, arrose, resurface,
                        nom_pat))
        return cursor.fetchall()

    # Cree une condition
    def add_condition(self, date_heure, ouvert, deblaye, arrose, resurface,
                      nom_pat):
        connect = self.get_connection()
        cursor = connect.cursor()
        try:
            cursor.execute(("INSERT INTO condition(date_heure, ouvert, deblaye, \
                        arrose, resurface, nom_pat)" "values(?,?,?,?,?,?)"),
                        (date_heure, ouvert, deblaye, arrose,
                        resurface, nom_pat))
            connect.commit()
        except:
            connect.rollback()

    def get_one_arrondissement(self, nom_arr):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM arrondissement WHERE nom_arr=?",
                       (nom_arr,))
        return cursor.fetchone()

    def get_all_arrondissement(self):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM arrondissement")
        return cursor.fetchall()

    # Recherche les glissades selon un nom d'arrondissement
    def find_glissade_arrondissement(self, requete):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM glissade WHERE nom_arr LIKE ?",
                       ('%'+requete+'%',))
        reponse_json = []
        glissade = cursor.fetchall()
        for r in glissade:
            arrondissement = Database().get_one_arrondissement(r[4])
            d = collections.OrderedDict()
            d["nom"] = r[0]
            d["nom_arr"] = arrondissement[0]
            d["cle"] = arrondissement[1]
            d["date_maj"] = arrondissement[2]
            d["ouvert"] = r[1]
            d["deblaye"] = r[2]
            d["condition"] = r[3]
            reponse_json.append(d)
        return json.dumps(reponse_json, ensure_ascii=False)

    # Recherche les patinoires selon un nom d'arrondissement
    def find_patinoire_arrondissement(self, requete):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM patinoire WHERE nom_arr LIKE ?",
                       ('%'+requete+'%',))
        reponse_json = []
        patinoire = cursor.fetchall()
        for r in patinoire:
            d = collections.OrderedDict()
            d["nom_arr"] = r[0].strip()
            d["nom_pat"] = r[1].strip()
            reponse_json.append(d)
        return json.dumps(reponse_json, ensure_ascii=False)

    # Recherche les piscines selon un nom d'arrondissement
    def find_piscine_arrondissement(self, requete):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM piscine WHERE arrondisse LIKE ?",
                       ('%'+requete+'%',))
        reponse_json = []
        piscine = cursor.fetchall()
        for r in piscine:
            d = collections.OrderedDict()
            d["id_uev"] = r[0]
            d["type"] = r[1]
            d["nom"] = r[2]
            d["arrondisse"] = r[3]
            d["adresse"] = r[4]
            d["propriete"] = r[5]
            d["gestion"] = r[6]
            d["point_x"] = r[7]
            d["point_y"] = r[8]
            d["equipeme"] = r[9]
            d["long"] = r[10]
            d["lat"] = r[11]
            reponse_json.append(d)
        return json.dumps(reponse_json, ensure_ascii=False)

    def valider_user(self, user):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM user WHERE user=?", (user,))
        return cursor.fetchall()

    def valider_email(self, email):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM user WHERE email=?", (email,))
        return cursor.fetchall()

    def create_user(self, user, email, salt, hash, arrondissements):
        connect = self.get_connection()
        cursor = connect.cursor()
        try:
            cursor.execute(("INSERT INTO user(user, email, salt, hash, \
                            arrondissements)" "values(?,?,?,?,?)"),
                        (user, email, salt, hash, arrondissements))
            connect.commit()
        except:
            connect.rollback()

    def get_noms_installations(self):
        connect = self.get_connection()
        cursor = connect.cursor()
        var = cursor.execute("SELECT nom FROM glissade").fetchall()
        var = var + cursor.execute("SELECT nom FROM piscine").fetchall()
        var = var + cursor.execute("SELECT nom_pat FROM patinoire").fetchall()
        var = [x[0] for x in var]
        return json.dumps(var, ensure_ascii=False)

    def get_info_by_nom_installation(self, nom):
        connect = self.get_connection()
        cursor = connect.cursor()
        var = cursor.execute("SELECT * FROM glissade WHERE nom=?", (nom,)).fetchone()
        if (var == None):
            var = cursor.execute("SELECT * FROM piscine WHERE nom=?", (nom,)).fetchone()
            if (var == None):
                var = cursor.execute("SELECT * FROM patinoire WHERE nom_pat=?", (nom,)).fetchone()
        return json.dumps(var, ensure_ascii=False)
