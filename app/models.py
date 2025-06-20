from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Initialize database here to avoid circular imports
db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def load_challenges_by_category(category_name):
    with open('data/challenges.json', encoding='utf-8') as f:
        all_challenges = json.load(f)
    return [ch for ch in all_challenges if ch['category'].lower() == category_name.lower()]

def load_challenges_by_category(category_name):
    with open('data/challenges.json') as f:
        data = json.load(f)
    return [ch for ch in data if ch["category"].lower() == category_name.lower()]

class UserChallengeProgress(db.Model):
    __tablename__ = 'challenge_progress'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False)  # adjust type if you use real user accounts
    challenge_id = db.Column(db.String(64), nullable=False)
    status = db.Column(db.String(20), default="started")  # options: started, completed, failed
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    score = db.Column(db.Float, nullable=True)
    attempts = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Progress user={self.user_id} challenge={self.challenge_id} status={self.status}>'

class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False)
    level = db.Column(db.String(32), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

