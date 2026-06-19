# Blueprint "main" : contient les routes générales (accueil, à propos, etc.)
# Un Blueprint est un module de routes indépendant qu'on branche sur l'app principale.

from flask import Blueprint

main_bp = Blueprint("main", __name__, template_folder="../../templates")

from . import routes  # noqa : import nécessaire pour enregistrer les routes
