from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

import os

# General
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Auth
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'

from project.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


# Blueprints
from project.users import users_bp

app.register_blueprint(users_bp)


# General views
from . import views

db.create_all()
