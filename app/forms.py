# Les formulaires Flask-WTF combinent la définition du formulaire HTML
# et la validation des données côté serveur en un seul endroit.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    # DataRequired : le champ ne peut pas être vide
    # Length : le titre doit faire entre 3 et 100 caractères
    title = StringField(
        "Titre de la tâche",
        validators=[DataRequired(message="Le titre est obligatoire."),
                    Length(min=3, max=100)]
    )
    submit = SubmitField("Ajouter la tâche")
