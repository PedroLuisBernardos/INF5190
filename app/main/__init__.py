# __init__.py
# Defini le blueprint des autres routes
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
