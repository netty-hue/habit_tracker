from flask import render_template
from flask import render_template, redirect, url_for, flash
from app.forms import RegisterForm

def register_routes(app):

    @app.route("/")
    def onboarding():
        return render_template("scrollbar.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():

        form = RegisterForm()

        if form.validate_on_submit():
            flash("Account created successfully!", "success")
            return redirect(url_for("login"))

        return render_template(
            "register.html",
            form=form
        )

    @app.route("/login")
    def login():
        return render_template("login.html")

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")


