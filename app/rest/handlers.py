# handlers.py
# Defini les routes des requetes REST
from flask import render_template
from app.rest import bp
from app.rest.forms import NomInstallationForm
from app import Database


# Documentation de tous les services REST
@bp.route('/doc')
def doc():
    return render_template("rest/doc.html", title="Documentation REST")


# Affichage des installations selon un arrondissement
@bp.route('/api/installations/<arrondissement>')
def installations_arrondissement(arrondissement):
    glissades = Database().find_glissade_arrondissement(arrondissement)
    patinoires = Database().find_patinoire_arrondissement(arrondissement)
    piscines = Database().find_piscine_arrondissement(arrondissement)
    return {'glissades':glissades,'patinoires':patinoires,'piscines':piscines}


@bp.route('/api/noms_installations/', methods=["GET", "POST"])
def noms_installations():
    form = NomInstallationForm()
    if form.validate_on_submit():
        new_form = NomInstallationForm()
        nom_installation = form.nom_installation.data
        return render_template("rest/noms_installations.html", title="Accueil",
                               nom_installation=nom_installation, form=new_form)
    return render_template('rest/noms_installations.html', title="Accueil",
                           form=form)


@bp.route('/api/installation/<nom>')
def info_nom_installation(nom):
    return Database().get_info_by_nom_installation(nom)
