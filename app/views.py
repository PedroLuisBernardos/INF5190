# views.py
# Contient les routes de l'application
from datetime import date
import re
from sqlite3.dbapi2 import TimeFromTicks
from flask import render_template, redirect, url_for, session, request
from app.database import Database
from app import app, get_db, schema, Config
from app.forms import ArrondissementForm, NomInstallationForm
import json

# Page principale
# Contient un formulaire pour afficher les installations selon un arrondissement
@app.route('/', methods=["GET", "POST"])
def index():
    form = ArrondissementForm()
    if form.validate_on_submit():
        new_form = ArrondissementForm()
        arrondissement = form.arrondissement.data
        return render_template("index.html", title="Accueil",
                               arrondissement=arrondissement, form=new_form)
    return render_template("index.html", title="Accueil", form=form)

# Modifie entierement une glissade selon un JSON recu
@app.route('/api/glissade/<nom_request>', methods=["PUT"])
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

        return Database().update_glissade(nom_request, nom, nom_arr_request, nom_arr, cle, date_maj, ouvert, deblaye, condition)
    else:
        return {'error': 'La glissade n\'existe pas'}, 404


# Modifie partiellement une glissade selon un JSON recu
@app.route('/api/glissade/<nom_request>', methods=["PATCH"])
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

        return Database().update_glissade(nom_request, nom, nom_arr_request, nom_arr, cle, date_maj, ouvert, deblaye, condition)
    else:
        return {'error': 'La glissade n\'existe pas'}, 404


# Modifie entierement une patinoire selon un JSON recu
#TODO
@app.route('/api/patinoire/<nom_request>', methods=["PUT"])
@schema.validate(Config.schema_create_patinoires)
def update_patinoires_put(nom_request):
    return nom_request


# Modifie entierement une piscine selon un JSON recu
#TODO
@app.route('/api/pisicne/<nom_request>', methods=["PUT"])
@schema.validate(Config.schema_create_piscines)
def update_piscines_put(nom_request):
    return nom_request


# Modifie partiellement une patinoire selon un JSON recu
#TODO
@app.route('/api/patinoire/<nom_request>', methods=["PATCH"])
@schema.validate(Config.schema_update_patinoires)
def update_patinoires_patch(nom_request):
    return nom_request


# Modifie partiellement une piscine selon un JSON recu
#TODO
@app.route('/api/pisicne/<nom_request>', methods=["PATCH"])
@schema.validate(Config.schema_update_piscines)
def update_piscines_patch(nom_request):
    return nom_request


# Contient un formulaire pour afficher l'information d'une installation selon son nom
@app.route('/noms_installations/', methods=["GET", "POST"])
def noms_installations():
    form = NomInstallationForm()
    if form.validate_on_submit():
        new_form = NomInstallationForm()
        nom_installation = form.nom_installation.data
        return render_template("noms_installations.html", title="Accueil",
                               nom_installation=nom_installation, form=new_form)
    return render_template('noms_installations.html', title="Accueil",
                           form=form)