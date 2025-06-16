from flask import Blueprint, render_template
from flask import request
from app.logic.challenges import challenges
from flask import flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app.models import db
import json
from flask import render_template


main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html", challenges=challenges)

@main.route("/challenge/<int:cid>", methods=["GET", "POST"])
def run_challenge(cid):
    from app.logic.challenges import challenges

    entry = challenges.get(cid)
    if not entry:
        return "Challenge not found", 404

    title, func, params = entry
    result = None

    if request.method == "POST":
        try:
            # Get inputs from form and convert to int/float if possible
            args = []
            for p in params:
                val = request.form.get(p, "")
                val = float(val) if "." in val else int(val)
                args.append(val)
            result = func(*args)
        except Exception as e:
            result = f"❗ Error: {e}"

    return render_template("challenge_form.html", cid=cid, title=title, params=params, result=result)


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

@main.route("/quiz/<level>")
def quiz(level):
    try:
        with open(f"data/{level}.json", "r", encoding="utf-8") as f:
            quizzes = json.load(f)
    except FileNotFoundError:
        quizzes = []
    return render_template("quiz.html", quizzes=quizzes, level=level.capitalize())
