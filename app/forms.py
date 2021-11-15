# forms.py
# Defini le formulaire du point A5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import ValidationError, DataRequired
from wtforms.validators import Email, Length, EqualTo
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
