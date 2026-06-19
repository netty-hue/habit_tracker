# Point d'entrée de l'application.
# On importe la factory et on crée l'app, puis on la lance.

from app import create_app
from flask import Flask, render_template, redirect, url_for, flash
from app.forms import RegisterForm

app = create_app()

app.config["SECRET_KEY"] = "your-secret-key"

@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        flash("Account created successfully!", "success")

        return redirect(url_for("register"))

    return render_template(
        "register.html",
        form=form
    )

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
app = Flask(__name__)