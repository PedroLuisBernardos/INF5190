# views.py
# Contient les routes de l'application
from sqlite3.dbapi2 import TimeFromTicks
from flask import render_template, redirect, url_for, session, request
from flask_login import current_user
from app import app, get_db, schema, Config
from app.forms import ArrondissementForm


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
@schema.validate(Config.glissades_update_shema)
def update_glissade(nom):
    if request.method == 'POST':
        return request.get_json()
    return nom
