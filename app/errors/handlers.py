# handlers.py
# Defini les erreurs possibles
from flask import render_template, jsonify
from app.errors import bp

@bp.errorhandler(404)
def page_not_found(error):
    return render_template("errors/error.html", title="Erreur",
                           error="404", message="Cette page n'existe pas"), 404

@bp.errorhandler(400)
def bad_request(error):
    return render_template("errors/error.html", title="Erreur",
                           error="400", message="Mauvaise requête"), 400


@bp.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/error.html', title="Erreur",
                           error="500", message="Erreur avec le serveur"), 500
