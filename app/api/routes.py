# handlers.py
# Defini les routes des requetes REST
from flask import render_template, current_app
from flask.globals import request
from config import Config
from app.api import bp
from app import database, schema, get_db
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
    #nom = nom.encode('raw_unicode_escape').decode('utf-8')
    glissade = database.Database().get_glissade(nom)
    if glissade == "null":
        return {'error': 'La glissade n\'existe pas'}, 404
    database.Database().delete_glissade(nom)
    return glissade


# Modifie entierement une glissade selon un JSON recu
@bp.route('/glissade/<nom_request>', methods=["PUT"])
@schema.validate(Config.schema_create_glissades)
def update_glissade_put(nom_request):
    # Si la glissade existe
    if get_db().get_glissade(nom_request) != "null":

        nom = request.get_json()['nom']
        nom_arr = request.get_json()['arrondissement']['nom_arr']
        cle = request.get_json()['arrondissement']['cle']
        date_maj = request.get_json()['arrondissement']['date_maj']
        ouvert = request.get_json()['ouvert']
        deblaye = request.get_json()['deblaye']
        condition = request.get_json()['condition']
        nom_arr_request = json.loads(get_db().get_glissade(nom_request))['arrondissement']['nom_arr']

        return database.Database().update_glissade(nom_request, nom, nom_arr_request, nom_arr, cle, date_maj, ouvert, deblaye, condition)
    else:
        return {'error': 'La glissade n\'existe pas'}, 404


# Modifie partiellement une glissade selon un JSON recu
@bp.route('/glissade/<nom_request>', methods=["PATCH"])
@schema.validate(Config.schema_update_glissades)
def update_glissade_patch(nom_request):
    # Si la glissade existe
    if get_db().get_glissade(nom_request) != "null":
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

        nom_arr_request = json.loads(get_db().get_glissade(nom_request))['arrondissement']['nom_arr']

        return database.Database().update_glissade(nom_request, nom, nom_arr_request, nom_arr, cle, date_maj, ouvert, deblaye, condition)
    else:
        return {'error': 'La glissade n\'existe pas'}, 404


@bp.route('/patinoires')
def patinoires():
    patinoires = database.Database().get_patinoires()
    if patinoires == "[]":
        return {'error': 'Il n\'y a aucune patinoire'}, 404
    return patinoires


@bp.route('/patinoire/<nom>')
def get_patinoire(nom):
    # nom = nom.encode('raw_unicode_escape').decode('utf-8')
    patinoire = database.Database().get_patinoire(nom)
    if patinoire == "null":
        return {'error': 'La patinoire n\'existe pas'}, 404
    return patinoire


@bp.route('/patinoire/<nom>', methods=['DELETE'])
def delete_patinoire(nom):
    try:
        # nom = nom.encode('raw_unicode_escape').decode('utf-8')
        patinoire = database.Database().get_patinoire(nom)
        if patinoire == "null":
            return {'error': 'La patinoire n\'existe pas'}, 404
        database.Database().delete_patinoire(nom)
        return patinoire
    except:
        return {'error': 'Il y a eu une erreur avec la suppression de la patinoire'}, 500

# Modifie entierement une patinoire selon un JSON recu
@bp.route('/patinoire/<nom_request>', methods=["PUT"])
@schema.validate(Config.schema_create_patinoires)
def update_patinoires_put(nom_request):
    # Si la patinoire existe
    if get_db().get_patinoire(nom_request) != "null":

        nom_pat = request.get_json()['nom_pat']
        nom_arr = request.get_json()['nom_arr']

        return database.Database().update_patinoire(nom_request, nom_pat, nom_arr)
    else:
        return {'error': 'La patinoire n\'existe pas'}, 404


# Modifie partiellement une patinoire selon un JSON recu
@bp.route('/patinoire/<nom_request>', methods=["PATCH"])
@schema.validate(Config.schema_update_patinoires)
def update_patinoires_patch(nom_request):
    # Si la patinoire existe
    if get_db().get_patinoire(nom_request) != "null":
        nom_pat = None
        nom_arr = None

        if 'nom_pat' in request.get_json():
            nom_pat = request.get_json()['nom_pat']
        if 'nom_arr' in request.get_json():
            nom_arr = request.get_json()['nom_arr']

        return database.Database().update_patinoire(nom_request, nom_pat, nom_arr)
    else:
        return {'error': 'La patinoire n\'existe pas'}, 404


@bp.route('/piscines')
def piscines():
    piscines = database.Database().get_piscines()
    if piscines == "[]":
        return {'error': 'Il n\'y a aucune piscine'}, 404
    return piscines


@bp.route('/piscine/<style>/<nom>')
def get_piscine(nom, style):
    # nom = nom.encode('raw_unicode_escape').decode('utf-8')
    piscine = database.Database().get_piscine(nom, style)
    if piscine == "null":
        return {'error': 'La piscine n\'existe pas'}, 404
    return piscine


@bp.route('/piscine/<style>/<nom>', methods=['DELETE'])
def delete_piscine(nom, style):
    try:
        # nom = nom.encode('raw_unicode_escape').decode('utf-8')
        piscine = database.Database().get_piscine(nom, style)
        if piscine == "null":
            return {'error': 'La piscine n\'existe pas'}, 404
        database.Database().delete_piscine(nom, style)
        return piscine
    except:
        return {'error': 'Il y a eu une erreur avec la suppression de la piscine'}, 500


# Modifie entierement une piscine selon un JSON recu
@bp.route('/piscine/<style_request>/<nom_request>', methods=["PUT"])
@schema.validate(Config.schema_create_piscines)
def update_piscines_put(nom_request, style_request):
    # Si la piscine existe
    if get_db().get_piscine(nom_request, style_request) != "null":

        if 'id_uev' in request.get_json():
            id_uev = request.get_json()['id_uev']
        if 'style' in request.get_json():
            style = request.get_json()['style']
        if 'nom' in request.get_json():
            nom = request.get_json()['nom']
        if 'arrondisse' in request.get_json():
            arrondisse = request.get_json()['arrondisse']
        if 'adresse' in request.get_json():
            adresse = request.get_json()['adresse']
        if 'propriete' in request.get_json():
            propriete = request.get_json()['propriete']
        if 'gestion' in request.get_json():
            gestion = request.get_json()['gestion']
        if 'point_x' in request.get_json():
            point_x = request.get_json()['point_x']
        if 'point_y' in request.get_json():
            point_y = request.get_json()['point_y']
        if 'equipeme' in request.get_json():
            equipeme = request.get_json()['equipeme']
        if 'longitude' in request.get_json():
            longitude = request.get_json()['longitude']
        if 'latitude' in request.get_json():
            latitude = request.get_json()['latitude']

        return database.Database().update_piscine(nom_request, style_request, id_uev, style, nom, arrondisse, adresse, propriete, gestion, point_x, point_y, equipeme, longitude, latitude)
    else:
        return {'error': 'La piscine n\'existe pas'}, 404

# Modifie partiellement une piscine selon un JSON recu
@bp.route('/piscine/<style_request>/<nom_request>', methods=["PATCH"])
@schema.validate(Config.schema_update_piscines)
def update_piscines_patch(nom_request, style_request):
    # Si la piscine existe
    if get_db().get_piscine(nom_request, style_request) != "null":
        id_uev = None
        style = None
        nom = None
        arrondisse = None
        adresse = None
        propriete = None
        gestion = None
        point_x = None
        point_y = None
        equipeme = None
        longitude = None
        latitude = None

        if 'id_uev' in request.get_json():
            id_uev = request.get_json()['id_uev']
        if 'style' in request.get_json():
            style = request.get_json()['style']
        if 'nom' in request.get_json():
            nom = request.get_json()['nom']
        if 'arrondisse' in request.get_json():
            arrondisse = request.get_json()['arrondisse']
        if 'adresse' in request.get_json():
            adresse = request.get_json()['adresse']
        if 'propriete' in request.get_json():
            propriete = request.get_json()['propriete']
        if 'gestion' in request.get_json():
            gestion = request.get_json()['gestion']
        if 'point_x' in request.get_json():
            point_x = request.get_json()['point_x']
        if 'point_y' in request.get_json():
            point_y = request.get_json()['point_y']
        if 'equipeme' in request.get_json():
            equipeme = request.get_json()['equipeme']
        if 'longitude' in request.get_json():
            longitude = request.get_json()['longitude']
        if 'latitude' in request.get_json():
            latitude = request.get_json()['latitude']

        return database.Database().update_piscine(nom_request, style_request, id_uev, style, nom, arrondisse, adresse, propriete, gestion, point_x, point_y, equipeme, longitude, latitude)
    else:
        return {'error': 'La piscine n\'existe pas'}, 404
