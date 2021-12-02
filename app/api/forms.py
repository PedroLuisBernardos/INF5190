# forms.py
# Defini le formulaire du point A5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField


class GlissadeForm(FlaskForm):
    nom = StringField('Nom')
    nom_arr = StringField('Nom de l\'arrondissement')
    cle = StringField('Cle')
    date_maj = StringField('Date')
    ouvert = IntegerField('Ouvert')
    deblaye = IntegerField('Deblaye')
    condition = StringField('Condition')
    modifier = SubmitField('Modifier')


class PatinoireForm(FlaskForm):
    nom_pat = StringField('Nom')
    nom_arr = StringField('Nom de l\'arrondissement')
    modifier = SubmitField('Modifier')


class PiscineForm(FlaskForm):
    id_uev = IntegerField('id_uev')
    style = StringField('Type')
    nom = StringField('Nom')
    arrondisse = StringField('Arrondissement')
    adresse = StringField('Adresse')
    propriete = StringField('Proprieté')
    gestion = StringField('Gestion')
    point_x = StringField('Point_X')
    point_y = StringField('Point_Y')
    equipeme = StringField('Equipement')
    longitude = DecimalField('Longitude', places=6)
    latitude = DecimalField('Latitude', places=6)
    modifier = SubmitField('Modifier')
