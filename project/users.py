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

@users_bp.route('/register', methods=['POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			username = form.username.data
			password = form.password.data
			displayname = form.displayname.data
			confirm_pass = form.confirm_pass.data
			user = User.query.filter_by(username=username).first()
			if user:
				print("name is taken")
				return "name taken"
			if password != confirm_pass:
				print("passwords do not match")
				return "passwords do not match"
			user = User(username, displayname, password)
			db.session.add(user)
			db.session.commit()
			login_user(user, remember=True)
			return redirect(url_for("feed"))
		else:
			return Response("<p>invalid form</p>")
	return render_template('login.html', form = form)
				

@users_bp.route('/register_test', methods=['POST'])
def register_test():
	form = RegisterForm(request.form)
	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		displayname = form.displayname.data
		confirm_pass = form.confirm_pass.data
		user = User.query.filter_by(username=username).first()
		if user:
			print("name is taken")
			return "name taken"
		if password != confirm_pass:
			print("passwords do not match")
			return "passwords do not match"
		user = User(username, displayname, password)
		db.session.add(user)
		db.session.commit()
		login_user(user, remember=True)
		return "success"
	else:
		return "nvalid form"

@users_bp.route('/login', methods=['GET', 'POST'])
@users_bp.route('/', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	print(form.username.data)
	print(form.password.data)
	if request.method == 'POST':
		if form.validate_on_submit():
			username = form.username.data
			password = form.password.data
			user = User.query.filter_by(username=username).first()
			if user is None or not user.check_password(password):
				return "wrong username or pass"
			login_user(user, remember=True)
			return redirect(url_for('feed'))
			#return render_template('index.html', user = user)
		else:
			return Response("<p>invalid login form</p>")
	return render_template('login.html', form = form)

@users_bp.route('/logout')
@login_required
def logout():
	logout_user()

	return Response("<p>Logged out</p>")



