# handlers.py
# Defini les routes des requetes REST
from flask import render_template
from flask.globals import request
from flask.helpers import url_for
from flask.json import jsonify
from werkzeug.utils import redirect
from config import Config
from app.rest import bp
from app import Database

# Documentation de tous les services REST
@bp.route('/doc')
def doc():
    return render_template("rest/doc.html", title="Documentation REST")


# Affichage des installations
# Un paramètre 'arrondissement' peut être specifie en parametres
@bp.route('/api/installations/')
def installations_arrondissement():
    arrondissement = request.args.get("arrondissement")
    if not arrondissement and request.args:
        return {'error': 'Le seul paramètre possible est arrondissement'}, 400
    elif 'arrondissement' in request.args:
        glissades = Database().find_glissade_arrondissement(arrondissement)
        patinoires = Database().find_patinoire_arrondissement(arrondissement)
        piscines = Database().find_piscine_arrondissement(arrondissement)
        if glissades == "[]" and patinoires == "[]" and piscines == "[]":
            return {'error': 'Aucune installation n\'a été trouvée'}, 404
        return {'glissades':glissades,'patinoires':patinoires,'piscines':piscines}
    else:
        glissades = Database().get_glissades()
        patinoires = Database().get_patinoires()
        piscines = Database().get_piscines()
        if glissades == "[]" and patinoires == "[]" and piscines == "[]":
            return {'error': 'Aucune installation n\'a été trouvée'}, 404
        return {'glissades': glissades,'patinoires': patinoires,'piscines': piscines}


@bp.route('/api/installation/<nom>')
def info_nom_installation(nom):
    nom = nom.encode('raw_unicode_escape').decode('utf-8')
    info = Database().get_info_by_nom_installation(nom)
    if info == "null":
        return {'error': 'Aucune installation n\'a été trouvée'}, 404
    return info


@bp.route('/api/glissades')
def glissades():
    glissades = Database().get_glissades()
    if glissades == "[]":
        return {'error': 'Il n\'y a aucune glissade'}, 404
    return glissades


@bp.route('/api/glissade/<nom>')
def get_glissade(nom):
    nom = nom.encode('raw_unicode_escape').decode('utf-8')
    glissade = Database().get_glissade(nom)
    if glissade == "null":
        return {'error': 'La glissade n\'existe pas'}, 404
    return glissade


@bp.route('/api/glissade/<nom>', methods=['DELETE'])
def delete_glissade(nom):
    try:
        nom = nom.encode('raw_unicode_escape').decode('utf-8')
        glissade = Database().get_glissade(nom)
        if glissade == "null":
            return {'error': 'La glissade n\'existe pas'}, 404
        Database().delete_glissade(nom)
        return glissade
    except:
        return {'error': 'Il y a eu une erreur avec la suppression de la glissade'}, 500
