# Contient les routes de l'application
from flask import render_template
from app.main.forms import ArrondissementForm, NomInstallationForm
from app.main import bp


# Page principale
# Contient un formulaire pour afficher les
# installations selon un arrondissement
@bp.route('/', methods=["GET", "POST"])
def index():
    form = ArrondissementForm()
    if form.validate_on_submit():
        new_form = ArrondissementForm()
        arrondissement = form.arrondissement.data
        return render_template("index.html",
                               title="Installations selon arrondissement",
                               arrondissement=arrondissement, form=new_form)
    return render_template("index.html",
                           title="Installations selon arrondissement",
                           form=form)


# Documentation de tous les services REST
@bp.route('/doc')
def doc():
    return render_template("api/doc.html", title="Documentation REST")


# Contient un formulaire pour afficher l'information
# d'une installation selon son nom
@bp.route('/noms_installations/', methods=["GET", "POST"])
def noms_installations():
    form = NomInstallationForm()
    if form.validate_on_submit():
        new_form = NomInstallationForm()
        nom_installation = form.nom_installation.data
        return render_template("noms_installations.html",
                               title="Accueil",
                               nom_installation=nom_installation,
                               form=new_form)
    return render_template('noms_installations.html',
                           title="Installation selon nom",
                           form=form)
