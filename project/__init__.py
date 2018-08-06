from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')


db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'

from project.models import User, Post

@login_manager.user_loader
def load_user(user_id):
	return User.query.filter(User.id == int(user_id)).first()

# Blueprints
from project.users import users_bp
from project.add_post import post_bp
from project.profile import profile_bp
app.register_blueprint(users_bp)
app.register_blueprint(post_bp)
app.register_blueprint(profile_bp)

# General views
from . import views

db.create_all()
