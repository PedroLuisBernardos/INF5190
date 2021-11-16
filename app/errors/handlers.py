# handlers.py
# Defini les erreurs possibles
from flask import render_template, jsonify
from flask_json_schema import JsonValidationError
from app.errors import bp

@bp.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({ 'error': e.message,
                    'errors': [validation_error.message for
                               validation_error in e.errors] })


@bp.errorhandler(404)
def page_not_found(error):
    return render_template("errors/error.html", title="Erreur",
                           error="404", message="Cette page n'existe pas"), 404


@bp.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/error.html', title="Erreur",
                           error="500", message="Erreur avec le serveur"), 500
