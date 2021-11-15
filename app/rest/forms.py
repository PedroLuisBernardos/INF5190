# forms.py
# Defini les formulaires en lien avec les requetes REST
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from app import Database


class NomInstallationForm(FlaskForm):
    choix = Database().get_noms_installations().split('"')
    choix = choix[1::2]
    choix = choix[1:-1]
    nom_installation = SelectField('Nom de l\'installation,',
                                   choices=choix)
    submit = SubmitField('Rechercher')