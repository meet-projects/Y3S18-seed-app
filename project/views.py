from flask import render_template, request, session, redirect, url_for
from flask_login import login_required
from project.forms import AddContactForm
from project import db
from project.models import User

from sqlalchemy import update
import os
from twilio.rest import Client
import threading
from project.tasks import alert, revoke
#from celery.task.control import revoke

from . import app

#NEED = 0
#USER = 0

'''
#Mahd's phone:
ACC_SID = "ACefef234a7dcd3cb22413db1ecab742a5"
AUTH_TOKEN = "4a6cd830f3a7b69ec5cae4fde76e34b9"
FROM = "+18604312585"
BODY = "YOUR BABY MIGHT BE IN DANGER! CHECK YOUR CAR!"

'''

#Mahd's phone:
ACC_SID = "ACefef234a7dcd3cb22413db1ecab742a5"
AUTH_TOKEN = "4a6cd830f3a7b69ec5cae4fde76e34b9"
FROM = "+18647546228"
BODY = "YOUR BABY MIGHT BE IN DANGER! CHECK YOUR CAR!"

@app.route('/')
def index():
	return render_template('landingpage.html')



@app.route('/hello')
def function():
	return render_template ('sendmessage.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/account', methods=['GET'])
@login_required
def account():
	form = AddContactForm(request.form)
	user = User.query.filter_by(id=session['user_id']).first()
	session['user_id'] = user.id
	return render_template('private.html', user=user, form=form)

@app.route('/test')
@login_required
def check():
	user = User.query.filter_by(username=session['name']).first()
	user.flag = 1
	db.session.commit()

@app.route('/private', methods=['GET','POST'])
@login_required
def private():

	return redirect(url_for('account'))

@app.route('/add_contact/<int:contact_num>', methods=['POST'])
def add_contact(contact_num):
	# form = AddContactForm(request.form)
	print(request.form)
	user = User.query.filter_by(id=session['user_id']).first()
	if (contact_num == 1):
		user.name1 = request.form['name1']
		user.relation1 = request.form['relation1']
		user.phone1 = request.form['phone1']
	elif (contact_num==2):
		user.name2 = request.form['name2']
		user.relation2 = request.form['relation2']
		user.phone2 = request.form['phone2']
	elif (contact_num==3):
		user.name3 = request.form['name3']
		user.relation3 = request.form['relation3']
		user.phone3 = request.form['phone3']
	else:
		return redirect(url_for('account'))
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




@app.route('/booster_seat_alert/<string:booster_seat_id>', methods=["GET","POST"])
def booster_seat_alert(booster_seat_id):
	user = User.query.filter_by(booster_seat_id=booster_seat_id).first()
	if request.method == "POST":
		user = User.query.filter_by(booster_seat_id=booster_seat_id).first()
		user.flag = 1
		if user.relation3:
			revoke(user.relation3)
		task = alert.delay(user.number, user.flag, user.phone1, user.phone2, user.phone3)
		print(type(task.id))
		user.relation3 = str(task.id)
		db.session.commit()
		return redirect(url_for('booster_seat_stop', booster_seat_id = booster_seat_id))
	else:
		return render_template('sendmessage.html' ,booster_seat_id = booster_seat_id, user=user)

	
	##GET : show a button on a template which will send POST request for this booster
	## POST: set flag to 1 for the user this booster belongs to


@app.route('/booster_seat_stop/<string:booster_seat_id>', methods=["GET","POST"]) 
def booster_seat_stop(booster_seat_id):
	user = User.query.filter_by(booster_seat_id=booster_seat_id).first()
	if request.method == 'POST':
		user = User.query.filter_by(booster_seat_id=booster_seat_id).first()
		user.flag = 0
		task = user.relation3
		print('before ' + task)
		revoke(task)
		print('revoked')
		user.relation3 = 0
		db.session.commit()
		return redirect(url_for('booster_seat_alert', booster_seat_id=booster_seat_id))	
	else:
		return render_template('stopmessage.html',booster_seat_id=booster_seat_id, user = user)

	##GET : show a button on a template which will send POST request for this booster
 	# POST: set flag to 0 for the user this booster belongs to

