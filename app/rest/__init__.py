# __init__.py
# Defini le blueprint des requetes REST
from flask import Blueprint

bp = Blueprint('rest', __name__)

from app.rest import handlers
