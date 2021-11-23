# __init__.py
# Defini le blueprint des requetes REST
from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import routes
