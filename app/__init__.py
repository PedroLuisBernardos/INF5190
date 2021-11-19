# __init__.py
from io import DEFAULT_BUFFER_SIZE
from flask import Flask, g
from config import Config
from flask_bootstrap import Bootstrap
from .database import Database
from app.errors import bp as errors_bp
from app.rest import bp as rest_bp
from flask_json_schema import JsonSchema
from apscheduler.schedulers.background import BackgroundScheduler
from os.path import exists
import re

app = Flask(__name__, static_url_path="", static_folder="static")
app.config.from_object(Config)
app.config['SECRET KEY'] = Config.SECRET_KEY
bootstrap = Bootstrap(app)
schema = JsonSchema(app)

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

from app.set_up import SetUp

# Creer la base de donnees
with app.app_context():
    if (exists("app/static/piscines.csv") and
        exists("app/static/patinoires.xml") and
            exists("app/static/glissades.xml")):
        schedule = BackgroundScheduler(daemon=True)
        schedule.add_job(SetUp.telecharger, 'cron', day='*', hour='0')
        schedule.start()
        # TODO update bd apres un chanegemtn??
    else:
        SetUp.telecharger()
        SetUp.create_piscine_db()
        SetUp.create_patinoire_db()
        SetUp.create_glissade_db()

# Gestion des erreurs
app.register_blueprint(errors_bp)

# Gestion des requetes REST
app.register_blueprint(rest_bp)

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=true)

from app import views
