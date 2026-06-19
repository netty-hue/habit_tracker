# Blueprint "tasks" : contient toutes les routes liées aux tâches.
# Préfixe URL "/tasks" défini dans create_app() → toutes les routes ici commencent par /tasks

from flask import Blueprint

tasks_bp = Blueprint("tasks", __name__, template_folder="../../templates")

from . import routes  # noqa
