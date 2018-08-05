from flask import (
		Blueprint, redirect, render_template, session,
		Response, request, url_for
)
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError

from project import db
from project.forms import RegisterForm, LoginForm, AddContactForm
from project.models import User


users_bp = Blueprint('users', __name__)

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST':
		username=form.username.data
		password = form.password.data
		number = form.number.data
		booster_seat_id = form.booster_seat_id.data   
		user = User.query.filter_by(username=username).first()
		if user:
			return Response("<p>Username already exists</p>")
		user = User(username, password, number, booster_seat_id)
		db.session.add(user)
		db.session.commit()
		login_user(user, remember=True)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '': 
			next_page = url_for('account')
		return redirect(url_for('account'))
	return render_template('register.html', form=form)
				

@users_bp.route('/login', methods=['GET', 'POST'])
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
			next_page = request.args.get('next')
			if not next_page or url_parse(next_page).netloc != '':
				next_page = url_for('account')
			return redirect(next_page)
		else:
			return Response("<p>invalid form</p>")
	return render_template('login.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
	logout_user()
	return Response("<p>Logged out</p>")


@users_bp.route('/add_contact', methods=['POST'])
def add_contact():
	# form = AddContactForm(request.form)
	print(request.form)
	user = User.query.filter_by(id=session['user_id']).first()
	user.name1 = request.form['name']
	user.relation1 = request.form['relation']
	user.phone1 = request.form['phone']
	db.session.commit()
	'''if request.method == 'POST':
		print(form)'''
	return redirect(url_for('account'))
	'''name=form.name.data
	relation = form.relation.data
	number= form.number.data'''
	'''user = User.query.filter_by(username=username).first()
	user = User(name, relation, number)
	db.session.add(user)
	db.session.commit()
	login_user(user, remember=True)
	next_page = request.args.get('next')
	if not next_page or url_parse(next_page).netloc != '':
		next_page = url_for('account')
	return redirect(url_for('account'))'''

