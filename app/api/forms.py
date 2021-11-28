# forms.py
# Defini le formulaire du point A5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length, ValidationError
import re

# TODO
class GlissadeForm(FlaskForm):
    m = "todo"
    e = "todo"
    nom = StringField('Nom', validators=[DataRequired(message=m),
                            Length(min=1, max=255, message=e)])
    nom_arr = StringField('Nom de l\'arrondissement', validators=[DataRequired(message=m),
                            Length(min=1, max=255, message=e)])
    cle = StringField('Cle', validators=[DataRequired(message=m),
                            Length(min=1, max=5, message=e)])
    date_maj = StringField('Date', validators=[DataRequired(message=m),
                            Length(min=1, max=255, message=e)])
    ouvert = IntegerField('Ouvert', validators=[DataRequired(message=m),
                            Length(min=0, max=1, message=e)])
    deblaye = IntegerField('Deblaye', validators=[DataRequired(message=m),
                            Length(min=0, max=1, message=e)])
    condition = StringField('Condition', validators=[DataRequired(message=m),
                            Length(min=1, max=255, message=e)])
    submit = SubmitField('Modifier')

    # Valier le format de la date
    def validate_date_maj(self, date_maj):
        date_maj = date_maj.data
        pattern = "%Y-%m-%dT%H:%M:%S.%fZ"
        match = re.search(pattern, date_maj)
        if not match:
            raise ValidationError('Veuillez entrer un format de date qui respecte le format ISO8601')

# TODO
class PatinoireForm(FlaskForm):
    m = "Veuillez entrer un nom d'arrondissement"
    e = "Vous devez entrer entre 1 et 100 caractères"
    nom_pat = StringField('Nom', validators=[DataRequired(message=m),
                             Length(min=1, max=255, message=e)])
    nom_arr = StringField('Nom de l\'arrondissement', validators=[DataRequired(message=m),
                             Length(min=1, max=255, message=e)])
    submit = SubmitField('Modifier')

# TODO
class PiscineForm(FlaskForm):
    m = "Veuillez entrer un nom d'arrondissement"
    e = "Vous devez entrer entre 1 et 100 caractères"
    nom = StringField('Nom', validators=[DataRequired(message=m),
                             Length(min=1, max=255, message=e)])
    nom_arr = StringField('Nom de l\'arrondissement', validators=[DataRequired(message=m),
                             Length(min=1, max=255, message=e)])
    cle = StringField('Cle', validators=[DataRequired(message=m),
                             Length(min=1, max=5, message=e)])
    date_maj = DateTimeField('Nom', format='%Y-%m-%d %H:%M', validators=[DataRequired(message=m),
                             Length(min=1, max=255, message=e)])
    ouvert = IntegerField('Ouvert', validators=[DataRequired(message=m),
                             Length(min=0, max=1, message=e)])
    deblaye = IntegerField('Deblaye', validators=[DataRequired(message=m),
                             Length(min=0, max=1, message=e)])
    condition = StringField('Condition', validators=[DataRequired(message=m),
                             Length(min=1, max=255, message=e)])
    submit = SubmitField('Modifier')
