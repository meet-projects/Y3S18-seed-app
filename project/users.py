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

@users_bp.route('/register', methods=['POST', 'GET'])
def register():
	print(request)
	form = RegisterForm(request.form)
	username = form.username.data
	password = form.password.data
	displayname = form.displayname.data
	if request.method == 'POST':
		print("reg submit")
		
		test_result = register_test(form)

		if test_result == "success":
			user = User(username, displayname, password)
			db.session.add(user)
			db.session.commit()
			login_user(user, remember=True)
			return redirect(url_for("feed"))

		else:
			data = {'show':'signup', 'err_msg':test_result}
			return render_template('login.html',form = form, data = data)
	else:
		print('opening reg page')
		data = {'show':'signup', 'err_msg':None}
		return render_template('login.html',form = form, data = data)
				
def register_test(form):
	username = form.username.data
	password = form.password.data
	displayname = form.displayname.data
	confirm_pass = form.confirm_pass.data

	if not username or username == '':
		return "username cannot be empty"

	if not displayname or displayname == '':
		return "display name cannot be empty"

	if not password or password == '':
		return "password cannot be empty"

	user = User.query.filter_by(username=username).first()
	if user:
		print("name is taken")
		return "name taken"
	if password != confirm_pass:
		print("passwords do not match")
		return "passwords do not match"
	# login_user(user, remember=True)
	return "success"

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
	return render_template('login.html',data={}, form = form)

@users_bp.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect('/')

