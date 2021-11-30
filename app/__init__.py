# __init__.py
from flask import Flask, g
from flask_bootstrap import Bootstrap
from flask_json_schema import JsonSchema
from config import Config
from .database import Database

app = Flask(__name__, static_url_path="", static_folder="static")
app.config.from_object(Config)
app.config['SECRET KEY'] = Config.SECRET_KEY
bootstrap = Bootstrap(app)
schema = JsonSchema(app)

with app.app_context():
    # Retourne la base de données
    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            g._database = Database()
        return g._database

    # Deconnecte la base de donnees qui est connectee
    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.disconnect()

    # Telecharge
    from app.scheduler import SetUp
    SetUp.run()

# Gestion des erreurs
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

# Gestion des requetes REST
from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

# Gestion des autres routes
from app.main import bp as main_bp
app.register_blueprint(main_bp)
