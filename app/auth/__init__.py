# __init__.py
# Defini le blueprint de l'authentification
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import handlers
