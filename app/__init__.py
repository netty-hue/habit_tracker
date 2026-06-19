# Application Factory : fonction qui crée et configure l'application Flask.
# Ce pattern évite d'avoir une app globale et facilite les tests et la scalabilité.

from flask import Flask
from .extensions import db
from .blueprints.main import main_bp
from .blueprints.tasks import tasks_bp


def create_app():
    app = Flask(__name__)

    # --- Configuration ---
    app.config["SECRET_KEY"] = "cle-secrete-a-changer-en-production"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # --- Initialisation des extensions ---
    db.init_app(app)

    # --- Enregistrement des Blueprints ---
    app.register_blueprint(main_bp)
    app.register_blueprint(tasks_bp, url_prefix="/tasks")

    # --- Création des tables si elles n'existent pas ---
    with app.app_context():
        db.create_all()

    return app
