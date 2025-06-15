from flask import Blueprint, render_template
from flask import request
from app.logic.challenges import sum_to_n, is_prime
from flask import flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app.models import db


main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/challenge/sum-to-n", methods=["GET", "POST"])
def challenge_sum_to_n():
    result = None
    if request.method == "POST":
        try:
            n = int(request.form.get("number"))
            result = sum_to_n(n)
        except:
            result = "Invalid input."
    return render_template("sum_to_n.html", result=result)

@main.route("/challenge/is-prime", methods=["GET", "POST"])
def challenge_is_prime():
    result = None
    if request.method == "POST":
        try:
            n = int(request.form.get("number"))
            result = f"{n} is {'a prime' if is_prime(n) else 'not a prime'} number."
        except:
            result = "Invalid input."
    return render_template("is_prime.html", result=result)

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("Username already exists.", "danger")
            return redirect(url_for("main.register"))
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created! You can now log in.", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f"Welcome back, {user.username}!", "success")
            return redirect(url_for("main.index"))
        flash("Invalid credentials.", "danger")
    return render_template("login.html", form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You’ve been logged out.", "info")
    return redirect(url_for("main.index"))