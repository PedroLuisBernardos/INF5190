# forms.py
# Defini les formulaires en lien avec l'authentification
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import ValidationError, DataRequired
from wtforms.validators import Email, Length, EqualTo
from app import Database


# Défini un formulaire pour la saisie de contacts
class UserForm(FlaskForm):
    m = "Veuillez entrer un nom"
    e = "Vous devez entrer entre 2 et 100 caractères"
    user = StringField('Nom', validators=[DataRequired(message=m),
                                          Length(min=2, max=100,
                                          message=e)])
    m = "Veuillez entrer une adresse courriel valide"
    e = 'Veuillez entrer une adresse courriel valide'
    email = StringField('Adresse courriel',
                        validators=[DataRequired(message=m), Email(message=e)])
    query = Database().get_all_arrondissement()
    arrondissements = SelectField('Arrondissements à surveiller',
                                  choices=[(0, "")] + [(q, q) for q in query],
                                  default=0)
    m = "Veuillez entrer un mot de passe valide"
    password = PasswordField('Mot de passe',
                             validators=[DataRequired(message=m)])
    m = "Veuillez entrer à nouveau votre mot de passe"
    e = "Les mots de passe ne sont pas identiques"
    password2 = PasswordField(
        'Entrez à nouveau votre mot de passe',
        validators=[DataRequired(message=m), EqualTo('password', message=e)])
    submit = SubmitField('Créer un compte')

    # Si le nom d'utilisateur existe déjà
    def validate_username(self, username):
        user = Database().valider_user(username.data)
        if user is not None:
            raise ValidationError('Ce nom d\'utilisateur est déjà utilisé')

    # Si le email existe déjà
    def validate_email(self, email):
        email = Database().valider_email(email.data)
        if email is not None:
            raise ValidationError('Cette adresse courriel est déjà utilisée')
