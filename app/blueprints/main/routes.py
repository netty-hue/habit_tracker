from flask import render_template
from . import main_bp


@main_bp.route("/")
def index():
    # Page d'accueil : simple, elle pointe vers le template main/index.html
    return render_template("main/index.html")
