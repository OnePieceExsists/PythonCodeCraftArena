from flask import Blueprint, render_template
from flask import request
from app.logic.challenges import challenges, load_all_challenges
from flask import flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import RegistrationForm, LoginForm
from app.models import User, QuizAttempt
from app.models import db
from app.models import UserChallengeProgress
import json, os
import random
from datetime import date
from flask import session

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

"""
@main.route('/quiz/<level>')
def quiz_view(level):
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    quiz_path = os.path.join(base, f"{level}_quiz.json")

    try:
        with open(quiz_path, 'r', encoding='utf-8') as f:
            quizzes = json.load(f)
    except Exception as e:
        print(f"❌ Failed to load quiz for {level}: {e}")
        quizzes = []

    return render_template('quiz.html', quizzes=quizzes, level=level)
"""

@main.route('/challenge/random')
def random_challenge():
    challenge_pool = load_all_challenges()
    level = random.choice(list(challenge_pool.keys()))
    challenge = random.choice(challenge_pool[level])
    return redirect(url_for('main.show_challenge', level=level, id=challenge['id']))

@main.route('/challenge/<level>/')
def list_challenges(level):
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    challenge_path = os.path.join(base, f"{level}.json")

    try:
        with open(challenge_path, 'r', encoding='utf-8') as f:
            challenges = json.load(f)
    except Exception as e:
        print(f"Error loading {level} challenges: {e}")
        challenges = []

    return render_template('challenge_list.html', level=level.capitalize(), challenges=challenges)

@main.route('/quiz/<level>', methods=["GET", "POST"])
def quiz_view(level):
    path = os.path.join(os.path.dirname(__file__), '..', 'data', f'{level.lower()}_quiz.json')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            quizzes = data["quiz"] if "quiz" in data else data
    except Exception as e:
        print(f"Error loading quiz data: {e}")
        quizzes = []

    if request.method == "POST":
        score = 0
        results = []

        print("✅ POST received and processed")

        for q in quizzes:
            user_answer = request.form.get(str(q['id']), '')
            correct = user_answer.strip().lower() == q['answer'].strip().lower()
            if correct:
                score += 1

            results.append({
                "question": q['question'],
                "your_answer": user_answer or "—",
                "correct_answer": q['answer'],
                "is_correct": correct
            })

        percentage = round(score / len(quizzes) * 100, 2)

        user_id = session.get("user_id")
        if not user_id:
            import uuid
            user_id = str(uuid.uuid4())
            session["user_id"] = user_id

        attempt = QuizAttempt(
            user_id=user_id,
            level=level.lower(),
            score=score,
            total=len(quizzes),
            percentage=percentage
        )
        db.session.add(attempt)
        db.session.commit()


        # Optional: Store result in database (QuizAttempt table)

        return render_template(
            'quiz_results.html',
            level=level.capitalize(),
            results=results,
            score=score,
            total=len(quizzes),
            percentage=percentage
        )

    return render_template('quiz.html', quizzes=quizzes, level=level.capitalize())

@main.route('/progress')
def view_progress():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for('main.index'))

    attempts = QuizAttempt.query.filter_by(user_id=user_id).order_by(QuizAttempt.timestamp.desc()).all()
    return render_template("progress.html", attempts=attempts)

@main.route('/challenge/<level>/<int:id>')
def show_challenge(level, id):
    path = os.path.join(os.path.dirname(__file__), '..', 'data', f'{level}.json')
    with open(path, 'r', encoding='utf-8') as f:
        all_challenges = json.load(f)
    
    if id < 1 or id > len(all_challenges):
        return "Challenge not found", 404

    challenge = all_challenges[id - 1]
    return render_template('challenge_viewer.html', challenge=challenge, level=level)

@main.route('/api/fetch_challenges/<level>', methods=['POST'])
def fetch_challenges(level):
    new_challenges = generate_challenges_by_level(level)

    path = os.path.join(os.path.dirname(__file__), '..', 'data', f'{level}.json')
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(new_challenges, f, indent=2)
        print(f"✅ Auto-generated {len(new_challenges)} {level} challenges.")
    except Exception as e:
        print(f"❌ Failed to write file: {e}")

    return redirect(url_for('main.list_challenges', level=level))

@main.route('/category/<category_name>')
def view_category(category_name):
    challenges = load_challenges_by_category(category_name)
    return render_template('category.html', challenges=challenges, category=category_name)

@main.route('/challenge/daily')
def daily_challenge():
    today_key = f"daily_{date.today().isoformat()}"

    if today_key not in session:
        with open("data/challenges.json") as f:
            challenges = json.load(f)
        challenge = random.choice(challenges)
        session[today_key] = challenge["id"]
    else:
        with open("data/challenges.json") as f:
            challenges = json.load(f)
        challenge = next((c for c in challenges if c["id"] == session[today_key]), None)

    return render_template("daily_challenge.html", challenge=challenge)

@main.route('/challenge/<challenge_id>', methods=['GET', 'POST'])
def challenge_view(challenge_id):
    # Fake or session-based user ID
    user_id = session.get("user_id")
    if not user_id:
        import uuid
        user_id = str(uuid.uuid4())
        session["user_id"] = user_id

    # Load challenge from JSON
    with open('data/challenges.json') as f:
        challenges = json.load(f)
    challenge = next((c for c in challenges if c["id"] == challenge_id), None)
    if not challenge:
        return "Challenge not found", 404

    # Track progress
    progress = UserChallengeProgress.query.filter_by(user_id=user_id, challenge_id=challenge_id).first()
    if request.method == "POST":
        user_code = request.form["user_code"]
        # Just mark as complete for now (later you can evaluate correctness)
        if not progress:
            progress = UserChallengeProgress(user_id=user_id, challenge_id=challenge_id, status="completed", attempts=1)
        else:
            progress.status = "completed"
            progress.attempts += 1
        db.session.add(progress)
        db.session.commit()

    output = None  # Initialize output before usage

    return render_template("challenge.html", challenge=challenge, challenge_id=challenge_id, progress=progress, output=output)

def load_challenges_by_category(category_name):
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'challenges.json')
    with open(path, 'r', encoding='utf-8') as f:
        all_challenges = json.load(f)
    return [ch for ch in all_challenges if ch.get("category", "").lower() == category_name.lower()]

def log_progress(user_id, challenge_id, status, score=None):
    progress = UserChallengeProgress.query.filter_by(user_id=user_id, challenge_id=challenge_id).first()
    if not progress:
        progress = UserChallengeProgress(user_id=user_id, challenge_id=challenge_id, status=status, score=score, attempts=1)
    else:
        progress.status = status
        progress.score = score
        progress.attempts += 1
    db.session.add(progress)
    db.session.commit()

def generate_challenges_by_level(level):
    level = level.lower()  # Normalize user input like 'Beginner' to 'beginner'

    if level == "beginner":
        return [
            {
                "title": "Echo Input",
                "description": "Prompt the user to enter a line of text, then print it back to them.",
                "tags": ["input", "output"]
            },
            {
                "title": "Celsius to Fahrenheit",
                "description": "Convert a Celsius temperature entered by the user into Fahrenheit using the formula F = C * 1.8 + 32.",
                "tags": ["math", "conversion"]
            },
            {
                "title": "Name in Uppercase",
                "description": "Ask the user for their name and display it in uppercase letters.",
                "tags": ["strings", "input", "manipulation"]
            },
            {
                "title": "Sum from 1 to n",
                "description": "Ask the user for a number n, then calculate and print the sum from 1 to n.",
                "tags": ["loops", "math"]
            },
            {
                "title": "Even or Odd",
                "description": "Ask the user for a number and tell them if it’s even or odd.",
                "tags": ["conditionals", "math"]
            },
            {
                "title": "Random Number Game",
                "description": "Generate a random number between 1 and 10. Let the user guess until they get it right.",
                "tags": ["loops", "random", "game"]
            },
            {
                "title": "Rectangle Area",
                "description": "Prompt for width and height, then calculate the area of a rectangle.",
                "tags": ["math", "geometry"]
            },
            {
                "title": "Countdown Timer",
                "description": "Ask for a number n and print numbers from n down to 1.",
                "tags": ["loops", "timing"]
            },
            {
                "title": "Simple Calculator",
                "description": "Ask the user for two numbers and an operator (+, -, *, /), then compute the result.",
                "tags": ["math", "conditionals"]
            },
            {
                "title": "Number Reverser",
                "description": "Ask the user for a number and print its digits in reverse.",
                "tags": ["math", "strings"]
            },
            {
                "title": "Word Length",
                "description": "Ask the user for a word and print how many letters it contains.",
                "tags": ["strings", "length"]
            },
            {
                "title": "Basic Tip Calculator",
                "description": "Ask for a bill amount and a tip percentage, then calculate the total.",
                "tags": ["math", "percentage"]
            },
            {
                "title": "Triangle Pattern",
                "description": "Print a triangle of asterisks with user-specified height.",
                "tags": ["loops", "patterns"]
            },
            {
                "title": "Last Digit Checker",
                "description": "Ask the user for a number and show the last digit of that number.",
                "tags": ["math", "modulo"]
            },
            {
                "title": "Random Password Generator",
                "description": "Generate a random password using letters, digits, and symbols.",
                "tags": ["random", "security"]
            }
        ]
    else:
        # Add intermediate, advanced, or pro generation here
        return []
