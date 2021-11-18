# forms.py
# Defini le formulaire du point A5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import NumberRange, DataRequired, Length
from app import Database


# Défini un formulaire pour la saisie de contacts
class ArrondissementForm(FlaskForm):
    m = "Veuillez entrer un nom d'arrondissement"
    e = "Vous devez entrer entre 1 et 100 caractères"
    arrondissement = StringField('Arrondissement',
                                 validators=[DataRequired(message=m),
                                 Length(min=1, max=100,
                                 message=e)])
    submit = SubmitField('Rechercher')


class NomInstallationForm(FlaskForm):
    choix = Database().get_noms_installations().split('"')
    choix = choix[1::2]
    choix = choix[1:-1]
    nom_installation = SelectField('Nom de l\'installation,',
                                   choices=choix)
    submit = SubmitField('Rechercher')