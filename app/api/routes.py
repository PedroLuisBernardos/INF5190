# handlers.py
# Defini les routes des requetes REST
from flask import render_template, current_app
from flask.globals import request
from config import Config
from app.api import bp
from app import database, schema
import json

# Affichage des installations
# Un paramètre 'arrondissement' peut être specifie en parametres
@bp.route('/installations')
def installations_arrondissement():
    arrondissement = request.args.get("arrondissement")
    if not arrondissement and request.args:
        return {'error': 'Le seul paramètre possible est arrondissement'}, 400
    elif 'arrondissement' in request.args:
        glissades = database.Database().find_glissade_arrondissement(arrondissement)
        patinoires = database.Database().find_patinoire_arrondissement(arrondissement)
        piscines = database.Database().find_piscine_arrondissement(arrondissement)
        if glissades == "[]" and patinoires == "[]" and piscines == "[]":
            return {'error': 'Aucune installation n\'a été trouvée'}, 404
        return {'glissades':glissades,'patinoires':patinoires,'piscines':piscines}
    else:
        glissades = database.Database().get_glissades()
        patinoires = database.Database().get_patinoires()
        piscines = database.Database().get_piscines()
        if glissades == "[]" and patinoires == "[]" and piscines == "[]":
            return {'error': 'Aucune installation n\'a été trouvée'}, 404
        return {'glissades': glissades,'patinoires': patinoires,'piscines': piscines}


@bp.route('/installation/<nom>')
def info_nom_installation(nom):
    nom = nom.encode('raw_unicode_escape').decode('utf-8')
    info = database.Database().get_info_by_nom_installation(nom)
    if info == "null":
        return {'error': 'Aucune installation n\'a été trouvée'}, 404
    return info


@bp.route('/glissades')
def glissades():
    glissades = database.Database().get_glissades()
    if glissades == "[]":
        return {'error': 'Il n\'y a aucune glissade'}, 404
    return glissades


@bp.route('/glissade/<nom>')
def get_glissade(nom):
    # nom = nom.encode('raw_unicode_escape').decode('utf-8')
    glissade = database.Database().get_glissade(nom)
    if glissade == "null":
        return {'error': 'La glissade n\'existe pas'}, 404
    return glissade


@bp.route('/glissade/<nom>', methods=['DELETE'])
def delete_glissade(nom):
    try:
        nom = nom.encode('raw_unicode_escape').decode('utf-8')
        glissade = database.Database().get_glissade(nom)
        if glissade == "null":
            return {'error': 'La glissade n\'existe pas'}, 404
        database.Database().delete_glissade(nom)
        return glissade
    except:
        return {'error': 'Il y a eu une erreur avec la suppression de la glissade'}, 500


# Modifie entierement une glissade selon un JSON recu
@bp.route('/glissade/<nom_request>', methods=["PUT"])
@schema.validate(Config.schema_create_glissades)
def update_glissade_put(nom_request):
    # Si la glissade existe
    if current_app.get_db().get_glissade(nom_request) != "null":

        nom = request.get_json()['nom']
        nom_arr = request.get_json()['arrondissement']['nom_arr']
        cle = request.get_json()['arrondissement']['cle']
        date_maj = request.get_json()['arrondissement']['date_maj']
        ouvert = request.get_json()['ouvert']
        deblaye = request.get_json()['deblaye']
        condition = request.get_json()['condition']
        nom_arr_request = json.loads(current_app.get_db().get_glissade(nom_request))['arrondissement']['nom_arr']

        return database.Database().update_glissade(nom_request, nom, nom_arr_request, nom_arr, cle, date_maj, ouvert, deblaye, condition)
    else:
        return {'error': 'La glissade n\'existe pas'}, 404


# Modifie partiellement une glissade selon un JSON recu
@bp.route('/glissade/<nom_request>', methods=["PATCH"])
@schema.validate(Config.schema_update_glissades)
def update_glissade_patch(nom_request):
    # Si la glissade existe
    if current_app.get_db().get_glissade(nom_request) != "null":
        nom = None
        nom_arr = None
        cle = None
        date_maj = None
        ouvert = None
        deblaye = None
        condition = None

        if 'nom' in request.get_json():
            nom = request.get_json()['nom']
        if 'arrondissement' in request.get_json():
            if 'nom_arr' in request.get_json()['arrondissement']:
                nom_arr = request.get_json()['arrondissement']['nom_arr']
            if 'cle' in request.get_json()['arrondissement']:
                cle = request.get_json()['arrondissement']['cle']
            if 'date_maj' in request.get_json()['arrondissement']:
                date_maj = request.get_json()['arrondissement']['date_maj']
        if 'ouvert' in request.get_json():
            ouvert = request.get_json()['ouvert']
        if 'deblaye' in request.get_json():
            deblaye = request.get_json()['deblaye']
        if 'condition' in request.get_json():
            condition = request.get_json()['condition']

        nom_arr_request = json.loads(current_app.get_db().get_glissade(nom_request))['arrondissement']['nom_arr']

        return database.Database().update_glissade(nom_request, nom, nom_arr_request, nom_arr, cle, date_maj, ouvert, deblaye, condition)
    else:
        return {'error': 'La glissade n\'existe pas'}, 404



@bp.route('/patinoires')
def patinoires():
    return ''


@bp.route('/patinoire/<nom>')
def get_patinoire(nom):
    return ''


@bp.route('/patinoire/<nom>', methods=['DELETE'])
def delete_patinoire(nom):
    return ''


# Modifie entierement une patinoire selon un JSON recu
#TODO
@bp.route('/patinoire/<nom_request>', methods=["PUT"])
@schema.validate(Config.schema_create_patinoires)
def update_patinoires_put(nom_request):
    return nom_request


# Modifie entierement une piscine selon un JSON recu
#TODO
@bp.route('/pisicne/<nom_request>', methods=["PUT"])
@schema.validate(Config.schema_create_piscines)
def update_piscines_put(nom_request):
    return nom_request


@bp.route('/piscines')
def piscines():
    return ''


@bp.route('/piscine/<nom>')
def get_piscine(nom):
    return ''


@bp.route('/piscine/<nom>', methods=['DELETE'])
def delete_piscine(nom):
    return ''


# Modifie partiellement une patinoire selon un JSON recu
#TODO
@bp.route('/patinoire/<nom_request>', methods=["PATCH"])
@schema.validate(Config.schema_update_patinoires)
def update_patinoires_patch(nom_request):
    return nom_request


# Modifie partiellement une piscine selon un JSON recu
#TODO
@bp.route('/pisicne/<nom_request>', methods=["PATCH"])
@schema.validate(Config.schema_update_piscines)
def update_piscines_patch(nom_request):
    return nom_request
