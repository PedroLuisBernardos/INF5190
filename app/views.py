# views.py
# Contient les routes de l'application
import re
from sqlite3.dbapi2 import TimeFromTicks
from flask import render_template, redirect, url_for, session, request
from app.database import Database
from app import app, get_db, schema, Config
from app.forms import ArrondissementForm, SchemaGlissadeForm


# Page principale
@app.route('/', methods=["GET", "POST"])
def index():
    username = None
    if "id" in session:
        username = get_db().get_session(session["id"])
    form = ArrondissementForm()
    if form.validate_on_submit():
        new_form = ArrondissementForm()
        arrondissement = form.arrondissement.data
        return render_template("index.html", title="Accueil",
                               arrondissement=arrondissement, form=new_form)
    return render_template("index.html", title="Accueil", form=form)

@app.route('/api/update/glissade/<nom>', methods=["GET", "POST"])
#@schema.validate(Config.schema)
def update_glissade_form(nom):
    form = SchemaGlissadeForm()
    if form.validate_on_submit() and request.method == 'POST':
        Database().update_glissade(nom, form.ouvert.data, form.deblaye.data, form.condition.data)
        return Database().get_glissade(nom)
    return render_template("glissades_schema.html", title="Accueil", form=form)
