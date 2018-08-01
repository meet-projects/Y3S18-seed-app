from flask import (
		Blueprint, redirect, render_template,
		Response, request, url_for , session
)
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError

from project import db
from project.forms import RegisterForm, LoginForm
from project.models import User


users_bp = Blueprint('users', __name__)

@users_bp.route('/register', methods=['POST'])
def register():
	form = RegisterForm(request.form)
	print(form.password.data)
	print(form.confirm_pass.data)
	if request.method == 'POST':
		if form.validate_on_submit():
			username = form.username.data
			password = form.password.data
			displayname = form.displayname.data
			confirm_pass = form.confirm_pass.data
			user = User.query.filter_by(username=username).first()
			if user is not None:
				return render_template('login.html', form = form, error_message="name taken")
			if password != confirm_pass:
				return render_template('login.html', form = form, error_message="passwords do not match")
			if user is None:
				user = User(username, displayname, password)
				db.session.add(user)
				db.session.commit()
				login_user(user, remember=True)
				return redirect(url_for("feed"))
		else:
			return Response("<p>invalid form</p>")
	return render_template('login.html', form = form)
				

@users_bp.route('/', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			username = form.username.data
			password = form.password.data
			user = User.query.filter_by(username=username).first()
			if user is None or not user.check_password(password):
				return render_template('login.html', form = form, error_message = "wrong username or pass")
			login_user(user, remember=True)
			return redirect(url_for('feed'))
		else:
			return Response("<p>invalid login form</p>")
	#if current_user:
	#	return redirect(url_for('feed'))
	#	return render_template('login.html', form = form)
	else:
		return render_template('login.html', form = form)


@users_bp.route('/logout')
@login_required
def logout():
	logout_user()

	return redirect()


