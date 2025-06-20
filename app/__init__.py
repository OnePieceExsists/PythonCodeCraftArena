from flask import Flask
from .routes import main
from flask_login import LoginManager
from app.models import db, User

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../instance/config.py")

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

login_manager.login_view = "main.login"
