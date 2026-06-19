from flask import render_template, redirect, url_for, flash
from . import tasks_bp
from ...extensions import db
from ...models import Task
from ...forms import TaskForm


@tasks_bp.route("/", methods=["GET", "POST"])
def index():
    form = TaskForm()

    # Si le formulaire est soumis et valide, on crée une nouvelle tâche
    if form.validate_on_submit():
        nouvelle_tache = Task(title=form.title.data)
        db.session.add(nouvelle_tache)
        db.session.commit()
        flash("Tâche ajoutée avec succès !", "success")
        return redirect(url_for("tasks.index"))

    # Récupère toutes les tâches en base de données
    taches = Task.query.all()
    return render_template("tasks/index.html", form=form, taches=taches)


@tasks_bp.route("/done/<int:task_id>")
def mark_done(task_id):
    # Récupère la tâche par son ID ou retourne une erreur 404 si introuvable
    tache = Task.query.get_or_404(task_id)
    tache.done = not tache.done   # Bascule l'état fait/non-fait
    db.session.commit()
    flash("Tâche mise à jour.", "info")
    return redirect(url_for("tasks.index"))


@tasks_bp.route("/delete/<int:task_id>")
def delete(task_id):
    tache = Task.query.get_or_404(task_id)
    db.session.delete(tache)
    db.session.commit()
    flash("Tâche supprimée.", "warning")
    return redirect(url_for("tasks.index"))
