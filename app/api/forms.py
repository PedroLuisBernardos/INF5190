# forms.py
# Defini le formulaire du point A5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, ValidationError
import re


# TODO TOUTES LES VALIDATIONS NE SE FONT PAS
class GlissadeForm(FlaskForm):
    m = "Ce champ est obligatoire"
    e = "Vous devez écrire entre 1 et 255 caractères"
    s = "Vous devez écrire soit 0 soit 1"
    nom = StringField('Nom', validators=[DataRequired(message=m),
                                         Length(min=1, max=255, message=e)])
    nom_arr = StringField('Nom de l\'arrondissement',
                          validators=[DataRequired(message=m),
                                      Length(min=1, max=255, message=e)])
    cle = StringField('Cle', validators=[DataRequired(message=m),
                                         Length(min=1, max=5, message=e)])
    date_maj = StringField('Date', validators=[DataRequired(message=m),
                                               Length(min=1, max=255,
                                               message=e)])
    ouvert = IntegerField('Ouvert', validators=[DataRequired(message=m),
                                                Length(min=0, max=1,
                                                message=s)])
    deblaye = IntegerField('Deblaye', validators=[DataRequired(message=m),
                                                  Length(min=0, max=1,
                                                  message=s)])
    condition = StringField('Condition', validators=[DataRequired(message=m),
                                                     Length(min=1,
                                                     max=255, message=e)])
    modifier = SubmitField('Modifier')

    # Valier le format de la date
    def validate_date_maj(self, date_maj):
        date_maj = date_maj.data
        pattern = "%Y-%m-%dT%H:%M:%S.%fZ"
        match = re.search(pattern, date_maj)
        if not match:
            raise ValidationError('Veuillez entrer un format de date qui '
                                  'respecte le format ISO8601')


class PatinoireForm(FlaskForm):
    m = "Ce champ est obligatoire"
    e = "Vous devez écrire entre 1 et 255 caractères"
    nom_pat = StringField('Nom', validators=[DataRequired(message=m),
                                             Length(min=1, max=255,
                                             message=e)])
    nom_arr = StringField('Nom de l\'arrondissement',
                          validators=[DataRequired(message=m),
                                      Length(min=1, max=255, message=e)])
    modifier = SubmitField('Modifier')


class PiscineForm(FlaskForm):
    m = "Ce champ est obligatoire"
    e = "Vous devez écrire entre 1 et 255 caractères"
    id_uev = IntegerField('id_uev', validators=[DataRequired(message=m)])
    style = StringField('Type', validators=[DataRequired(message=m),
                                            Length(min=1, max=255, message=e)])
    nom = StringField('Nom', validators=[DataRequired(message=m),
                                         Length(min=1, max=255, message=e)])
    arrondisse = StringField('Arrondissement',
                             validators=[DataRequired(message=m),
                                         Length(min=1, max=255, message=e)])
    adresse = StringField('Adresse')
    propriete = StringField('Proprieté')
    gestion = StringField('Gestion')
    point_x = StringField('Point_X', validators=[DataRequired(message=m)])
    point_y = StringField('Point_Y', validators=[DataRequired(message=m)])
    equipeme = StringField('Equipement', validators=[DataRequired(message=m),
                                                     Length(min=1, max=255,
                                                     message=e)])
    longitude = DecimalField('Longitude', places=6,
                             validators=[DataRequired(message=m)])
    latitude = DecimalField('Latitude', places=6,
                            validators=[DataRequired(message=m)])
    modifier = SubmitField('Modifier')

    # TODO validate format points et lat/long
