from apscheduler.schedulers.background import BackgroundScheduler
from os.path import exists
from app import create_app
from app.setup import bp as setup_bp

app = create_app()
app.app_context().push()

# Creer la base de donnees
if (exists("app/static/piscines.csv") and
    exists("app/static/patinoires.xml") and
        exists("app/static/glissades.xml")):
    schedule = BackgroundScheduler(daemon=True)
    schedule.add_job(setup_bp.telecharger, 'cron', day='*', hour='0')
    schedule.start()
    # TODO update bd apres un chanegemtn??
else:
    setup_bp.telecharger()
    setup_bp.create_piscine_db()
    setup_bp.create_patinoire_db()
    setup_bp.create_glissade_db()
