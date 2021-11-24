# __init__.py
from flask import Flask, current_app, g
from flask_bootstrap import Bootstrap
from flask_json_schema import JsonSchema
from .database import Database
from config import Config

bootstrap = Bootstrap()
schema = JsonSchema()

# Cree l'application
def create_app(config_class=Config):

    app = Flask(__name__, static_url_path="", static_folder="static")
    app.config.from_object(config_class)
    app.config['SECRET KEY'] = Config.SECRET_KEY
    bootstrap.init_app(app)
    schema.init_app(app)

    # Gestion des erreurs
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # Gestion des requetes REST
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # Gestion des autres routes
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Gestion du setup
    from app.setup import bp as setup_bp
    app.register_blueprint(setup_bp)

    return app

# Retourne la base de données
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


"""# Deconnecte la base de donnees qui est connectee
@current_app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()
"""