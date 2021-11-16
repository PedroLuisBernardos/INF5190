# forms.py
# Defini le formulaire du point A5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
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

class SchemaGlissadeForm(FlaskForm):
    m = "Vous devez choisir entre 0 (non) ou 1 (oui)"
    ouvert = IntegerField('Ouvert',
                          validators=[DataRequired(message=m),
                          NumberRange(min=0, max=1, message=m)])
    deblaye = IntegerField('Deblaye',
                          validators=[DataRequired(message=m),
                          NumberRange(min=0, max=1, message=m)])
    m = "Vous devez entrer une condition. Entrer 'N/A' sinon."
    condition = StringField('Condition', validators=[DataRequired(message=m)],
                            default="N/A")
    submit = SubmitField('Modifier')
