# Point d'entrée de l'application.
# On importe la factory et on crée l'app, puis on la lance.
from flask import Flask
from app.routes import register_routes

app = Flask(__name__)

app.config["SECRET_KEY"] = "your-secret-key"

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)