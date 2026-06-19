# On instancie les extensions ici, SANS les lier à une app.
# Elles seront liées plus tard via db.init_app(app) dans la factory.
# Cela évite les imports circulaires.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
