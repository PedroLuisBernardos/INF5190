# views.py
# Contient les routes de l'application
import re
from sqlite3.dbapi2 import TimeFromTicks
from flask import render_template, redirect, url_for, session, request
from app.database import Database
from app import app, get_db, schema, Config
from app.forms import ArrondissementForm, NomInstallationForm


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


@app.route('/api/glissade/<nom>', methods=["PUT", "PATCH"])
@schema.validate(Config.schema)
def update_glissade(nom):
    return request.get_json()


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