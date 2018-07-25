from flask import (
        Blueprint, redirect, render_template,
        Response, request, url_for
)
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError

from project import db
from project.forms import RegisterForm, LoginForm
from project.models import User

#import os
#from twilio.rest import Client

users_bp = Blueprint('users', __name__)


#ACC_SID = "ACd03777f4973c4f1ffc3efed677cc57b1"
#AUTH_TOKEN = "b22f0d66110237b42ebf63ccd2b4241e"
#TO = "+972529553327"
#FROM = "+972558820796"
#BODY = "YOUR BABY MIGHT BE IN DANGER! CHECK YOUR CAR!"

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
    	username=form.username.data
    	password = form.password.data
    	number = form.number.data
    	name = form.name.data
    	name1 = form.name1.data
    	name2 = form.name2.data
    	phone = form.phone.data
    	phone1 = form.phone1.data
    	phone2 = form.phone2.data
    	user = User.query.filter_by(username=username).first()
    	if user:
    		return Response("<p>Username already exists</p>")
    	user = User(username, password, number, name, name1, name2, phone, phone1, phone2)
    	db.session.add(user)
    	db.session.commit()
    	login_user(user, remember=True)
    	next_page = request.args.get('next')
    	if not next_page or url_parse(next_page).netloc != '':
    		next_page = url_for('private_route')
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
                next_page = url_for('private_route')
            return redirect(next_page)
        else:
            return Response("<p>invalid form</p>")
    return render_template('login.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return Response("<p>Logged out</p>")

@users_bp.route('/private', methods=['GET', 'POST'])
@login_required
def private_route():
	if request.method == 'POST':
#		account_sid = ACC_SID
#		auth_token = AUTH_TOKEN

#		client = Client(account_sid, auth_token)

#		client.messages.create(to=TO, from_=FROM, body=BODY) 

	return render_template('private.html')
