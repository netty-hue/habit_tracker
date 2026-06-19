# Flask Task App — Projet pédagogique L1
# Il est à modifier selon votre projet

## Arborescence du projet

```
flask_project/
├── run.py                        ← Point d'entrée : lance l'application
├── requirements.txt              ← Dépendances Python
└── app/
    ├── __init__.py               ← Application Factory (create_app)
    ├── extensions.py             ← Instances des extensions (db)
    ├── models.py                 ← Modèles SQLAlchemy (tables BDD)
    ├── forms.py                  ← Formulaires Flask-WTF
    ├── templates/
    │   ├── base.html             ← Template parent Jinja2
    │   ├── main/
    │   │   └── index.html        ← Page d'accueil
    │   └── tasks/
    │       └── index.html        ← Page liste + ajout de tâches
    ├── static/                   ← Fichiers CSS, JS, images (vide ici)
    └── blueprints/
        ├── main/
        │   ├── __init__.py       ← Déclaration du blueprint "main"
        │   └── routes.py         ← Routes : /
        └── tasks/
            ├── __init__.py       ← Déclaration du blueprint "tasks"
            └── routes.py         ← Routes : /tasks/, /tasks/done/<id>, /tasks/delete/<id>
```

## Installation et lancement

```bash
# 1. Créer un environnement virtuel
python -m venv venv

# 2. L'activer
# Sur Windows :
venv\Scripts\activate
# Sur macOS/Linux :
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
python run.py
```

Ouvrir le navigateur sur : **http://127.0.0.1:5000**

## Concepts illustrés

| Concept | Fichier(s) |
|---|---|
| Application Factory | `app/__init__.py` |
| Blueprint | `app/blueprints/*/` |
| Modèle SQLAlchemy | `app/models.py` |
| Formulaire Flask-WTF | `app/forms.py` |
| Template Jinja2 (héritage) | `app/templates/` |
| Extensions découplées | `app/extensions.py` |
