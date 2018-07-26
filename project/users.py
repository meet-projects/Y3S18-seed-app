from flask import (
        Blueprint, redirect, render_template,
        Response, request, url_for , session
)
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError

from project import db
from project.forms import RegisterForm, LoginForm
from project.models import User


users_bp = Blueprint('users', __name__)

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        print(form.validate_on_submit())
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            displayname = form.displayname.data
            user = User.query.filter_by(username=username).first()
            if user is None:
                user = User(username, displayname, password)
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("feed",  user=user))
        else:
            return Response("<p>invalid form</p>")
    return render_template('register.html', form=form)
                

@users_bp.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user is None or not user.check_password(password):
                return Response("<p>Incorrect username or password</p>")
            login_user(user, remember=True)
            return redirect(url_for('feed',  user=user))
            #return render_template('index.html', user = user)
        else:
            return Response("<p>invalid form!!!!!</p>")
    return render_template('login.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return Response("<p>Logged out</p>")

