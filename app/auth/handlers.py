# handlers.py
# Defini les routes de l'authentification
from flask import render_template, redirect
from app.auth import bp
from app.auth.forms import UserForm
from app.database import Database
import uuid
import hashlib


# Creation d'un compte
@bp.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    form = UserForm()
    if form.validate_on_submit():
        user = form.user.data
        email = form.email.data
        arrondissements = form.arrondissements
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(str(form.password.data +
                                             salt).encode("utf-8")).hexdigest()
        Database().create_user(user, email, salt, hashed_password,
                               arrondissements)
        return redirect("/")
    return render_template("auth/sign-up.html", title="S'inscrire", form=form)
