# forms.py
# Defini le formulaire du point A5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from app import Database

# Defini un formualire pour la recherche d'installations selon un arrondissement
class ArrondissementForm(FlaskForm):
    m = "Veuillez entrer un nom d'arrondissement"
    e = "Vous devez entrer entre 1 et 100 caractères"
    arrondissement = StringField('Arrondissement',
                                 validators=[DataRequired(message=m),
                                 Length(min=1, max=100,
                                 message=e)])
    submit = SubmitField('Rechercher')


# Defini un formualire pour la recherche d'informations sur une installation selon son nom
class NomInstallationForm(FlaskForm):
    choix = Database().get_noms_installations().split('"')
    choix = choix[1::2]
    choix = choix[1:-1]
    nom_installation = SelectField('Nom de l\'installation,',
                                   choices=choix)
    submit = SubmitField('Rechercher')