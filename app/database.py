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

    # Recherche si une glissade existe selon la cle primaire
    def is_glissade(self, nom):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM glissade WHERE nom=?", (nom,))
        return cursor.fetchall()

    # Cree une glissade dans la base de donnees
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

    # Construit un JSON d'une glissade
    def construire_json_glissade(self, cursor):
        reponse_json = []
        if cursor.__class__ == list:
            for r in cursor:
                arrondissement = Database().get_one_arrondissement(r[4])
                d = collections.OrderedDict()
                d["nom"] = r[0]
                d["arrondissement"] = {'nom_arr': arrondissement[0], 'cle': arrondissement[1], 'date_maj': arrondissement[2]}
                d["ouvert"] = r[1]
                d["deblaye"] = r[2]
                d["condition"] = r[3]
                reponse_json.append(d)
        else:
                arrondissement = Database().get_one_arrondissement(cursor[4])
                reponse_json = {'nom': cursor[0], 'arrondissement': {'nom_arr': arrondissement[0], 'cle': arrondissement[1], 'date_maj': arrondissement[2]}, 'ouvert': cursor[1], 'deblaye': cursor[2], 'condition': cursor[3]}
        return reponse_json

    # Recherche les glissades selon un nom d'arrondissement
    def find_glissade_arrondissement(self, requete):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM glissade WHERE nom_arr LIKE ?",
                       ('%'+requete+'%',))
        return json.dumps(Database().construire_json_glissade(cursor.fetchall()), ensure_ascii=False)

    # Supprime une glissade
    def delete_glissade(self, nom):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("DELETE FROM glissade WHERE nom=?", (nom,))
        connect.commit()

    # Retourne une glissade selon son nom
    def get_glissade(self, nom):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM glissade WHERE nom=?", (nom,))
        data = cursor.fetchone()
        if data == None:
            return "null"
        return json.dumps(Database().construire_json_glissade(data), ensure_ascii=False)

    # Retourne toutes les glissades
    def get_glissades(self):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM glissade")
        return json.dumps(Database().construire_json_glissade(cursor.fetchall()), ensure_ascii=False)

    # Modifie une glissade
    def update_glissade(self, nom_request, nom, nom_arr_request, nom_arr, cle, date_maj, ouvert, deblaye, condition):
        connect = self.get_connection()
        cursor = connect.cursor()
        try:
            if cle != None:
                cursor.execute("UPDATE arrondissement SET cle=? WHERE nom_arr=?", (cle, nom_arr_request))
            if date_maj != None:
                cursor.execute("UPDATE arrondissement SET date_maj=? WHERE nom_arr=?", (date_maj, nom_arr_request))
            if ouvert != None:
                cursor.execute("UPDATE glissade SET ouvert=? WHERE nom=?", (ouvert, nom_request))
            if deblaye != None:
                cursor.execute("UPDATE glissade SET deblaye=? WHERE nom=?", (deblaye, nom_request))
            if condition != None:
                cursor.execute("UPDATE glissade SET condition=? WHERE nom=?", (condition, nom_request))
            if nom != None:
                cursor.execute("UPDATE glissade SET nom=? WHERE nom=?", (nom, nom_request))
            if nom_arr != None:
                cursor.execute("UPDATE arrondissement SET nom_arr=? WHERE nom_arr=?", (nom_arr, nom_arr_request))
            connect.commit()
            if (nom == None):
                return Database().get_glissade(nom_request)
            return Database().get_glissade(nom)
        except:
            connect.rollback()

    # Recherche si un arrondissement existe selon la cle primaire
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

    # Retourne un arrondissement selon son nom
    def get_one_arrondissement(self, nom_arr):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM arrondissement WHERE nom_arr=?",
                       (nom_arr,))
        return cursor.fetchone()

    # Retourne tous les arrondissements
    def get_all_arrondissement(self):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM arrondissement")
        return cursor.fetchall()

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

    # Construit un JSON d'une patinoire
    def construire_json_patinoire(self, cursor):
        reponse_json = []
        if cursor.__class__ == list:
            for r in cursor:
                d = collections.OrderedDict()
                d["nom_arr"] = r[0].strip()
                d["nom_pat"] = r[1].strip()
                reponse_json.append(d)
        else:
            reponse_json = {'nom_arr': cursor[0].strip(), 'nom_pat': cursor[1].strip()}
        return reponse_json

    # Retourne les patinoires selon un nom d'arrondissement
    def find_patinoire_arrondissement(self, requete):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM patinoire WHERE nom_arr LIKE ?",
                       ('%'+requete+'%',))
        return json.dumps(Database().construire_json_patinoire(cursor.fetchall()), ensure_ascii=False)

    # Supprime une patinoire
    def delete_patinoire(self, nom):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("DELETE FROM patinoire WHERE nom_pat=?", (nom,))
        #connect.commit()

    # Retourne une patinoire selon son nom
    def get_patinoire(self, nom):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM patinoire WHERE nom_pat=?", (nom,))
        data = cursor.fetchone()
        if data == None:
            return "null"
        return json.dumps(Database().construire_json_patinoire(data), ensure_ascii=False)

    # Retourne toutes les patinoires
    def get_patinoires(self):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM patinoire")
        if cursor.fetchone() == None:
            return None
        return json.dumps(Database().construire_json_patinoire(cursor.fetchall()), ensure_ascii=False)

    # Modifie une patinoire
    def update_patinoire(self, nom_request, nom_pat, nom_arr):
        connect = self.get_connection()
        cursor = connect.cursor()
        try:
            if nom_arr != None:
                cursor.execute("UPDATE patinoire SET nom_arr=? WHERE nom_pat=?", (nom_arr, nom_request))
            if nom_pat != None:
                cursor.execute("UPDATE patinoire SET nom_pat=? WHERE nom_pat=?", (nom_pat, nom_request))
            connect.commit()
            if (nom_pat == None):
                return Database().get_patinoire(nom_request)
            return Database().get_patinoire(nom_pat)
        except:
            connect.rollback()

    """ Recherche si une condition existe, je l'ai commenté vu que je ne l'utilise pas
    def is_condition(self, date_heure, ouvert, deblaye, arrose, resurface,
                     nom_pat):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM condition WHERE \
                       date_heure=? and ouvert=? and deblaye=? and\
                       arrose=? and resurface=? and nom_pat=?",
                       (date_heure, ouvert, deblaye, arrose, resurface,
                        nom_pat))
        return cursor.fetchall()

    # Cree une condition, je l'ai commenté vu que je ne l'utilise pas
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
    """

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

    # Construit un JSON d'une piscine
    def construire_json_piscine(self, cursor):
        reponse_json = []
        if cursor.__class__ == list:
            for r in cursor:
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
        else:
            reponse_json = {'id_uev': cursor[0], 'type': cursor[1], 'nom': cursor[2], 'arrondisse': cursor[3], 'adresse': cursor[4], 'propriete': cursor[5], 'gestion': cursor[6], 'point_x': cursor[7], 'point_y': cursor[8], 'equipeme': cursor[9], 'long': cursor[10], 'lat': cursor[11]}
        return reponse_json

    # Recherche les piscines selon un nom d'arrondissement
    def find_piscine_arrondissement(self, requete):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM piscine WHERE arrondisse LIKE ?",
                       ('%'+requete+'%',))
        return json.dumps(Database().construire_json_piscine(cursor.fetchall()), ensure_ascii=False)

    # Supprime une piscine
    def delete_piscine(self, nom):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("DELETE FROM piscine WHERE nom=?", (nom,))
        #connect.commit()

    # Retourne une piscine selon son nom
    def get_piscine(self, nom):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM piscine WHERE nom=?", (nom,))
        data = cursor.fetchone()
        if data == None:
            return "null"
        return json.dumps(Database().construire_json_piscine(data), ensure_ascii=False)

    # Retourne toutes les piscines
    def get_piscines(self):
        connect = self.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM piscine")
        if cursor.fetchone() == None:
            return None
        return json.dumps(Database().construire_json_piscine(cursor.fetchall()), ensure_ascii=False)

    # Modifie une piscine
    def update_piscine(self, nom_request, id_uev, style, nom, arrondisse, adresse, propriete, gestion, point_x, point_y, equipeme, longitude, latitude):
        connect = self.get_connection()
        cursor = connect.cursor()
        try:
            if id_uev != None:
                cursor.execute("UPDATE piscine SET id_uev=? WHERE nom=?", (id_uev, nom_request))
            if style != None:
                cursor.execute("UPDATE piscine SET style=? WHERE nom=?", (style, nom_request))
            if arrondisse != None:
                cursor.execute("UPDATE piscine SET arrondisse=? WHERE nom=?", (arrondisse, nom_request))
            if adresse != None:
                cursor.execute("UPDATE piscine SET adresse=? WHERE nom=?", (adresse, nom_request))
            if propriete != None:
                cursor.execute("UPDATE piscine SET propriete=? WHERE nom=?", (propriete, nom_request))
            if gestion != None:
                cursor.execute("UPDATE piscine SET gestion=? WHERE nom=?", (gestion, nom_request))
            if point_x != None:
                cursor.execute("UPDATE piscine SET point_x=? WHERE nom=?", (point_x, nom_request))
            if point_y != None:
                cursor.execute("UPDATE piscine SET point_y=? WHERE nom=?", (point_y, nom_request))
            if equipeme != None:
                cursor.execute("UPDATE piscine SET equipeme=? WHERE nom=?", (equipeme, nom_request))
            if longitude != None:
                cursor.execute("UPDATE piscine SET longitude=? WHERE nom=?", (longitude, nom_request))
            if latitude != None:
                cursor.execute("UPDATE piscine SET latitude=? WHERE nom=?", (latitude, nom_request))
            if nom != None:
                cursor.execute("UPDATE piscine SET nom=? WHERE nom=?", (nom, nom_request))
            connect.commit()
            if (nom == None):
                return Database().get_piscine(nom_request)
            return Database().get_piscine(nom)
        except:
            connect.rollback()

    # Retourne tous les noms de toutes les installations
    def get_noms_installations(self):
        connect = self.get_connection()
        cursor = connect.cursor()
        var = cursor.execute("SELECT nom FROM glissade").fetchall()
        var = var + cursor.execute("SELECT nom FROM piscine").fetchall()
        var = var + cursor.execute("SELECT nom_pat FROM patinoire").fetchall()
        var = [x[0] for x in var]
        return json.dumps(var, ensure_ascii=False)

    # Recherche une installation par son nom et retourne l'info de la premiere trouvee
    def get_info_by_nom_installation(self, nom):
        connect = self.get_connection()
        cursor = connect.cursor()
        var = cursor.execute("SELECT * FROM glissade WHERE nom=?", (nom,)).fetchone()
        if (var == None):
            var = cursor.execute("SELECT * FROM piscine WHERE nom=?", (nom,)).fetchone()
            if (var == None):
                var = cursor.execute("SELECT * FROM patinoire WHERE nom_pat=?", (nom,)).fetchone()
                return json.dumps(Database().construire_json_patinoire(var), ensure_ascii=False)
            else:
                return json.dumps(Database().construire_json_piscine(var), ensure_ascii=False)
        return json.dumps(Database().construire_json_glissade(var), ensure_ascii=False)
