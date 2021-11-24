# app.py
# Defini l'instance de l'application Flask

from app import create_app

app = create_app()
app.app_context().push()

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=true)
