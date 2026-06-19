# Point d'entrée de l'application.
# On importe la factory et on crée l'app, puis on la lance.

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
