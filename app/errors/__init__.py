# __init__.py
# Defini le blueprint des erreurs
from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import routes
