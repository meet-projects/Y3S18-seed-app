from flask import render_template, request, session
from flask_login import login_required
from project.forms import AddContactForm

from project import db
from project.models import User

from sqlalchemy import update
import os
from twilio.rest import Client
import threading

from . import app

#NEED = 0
#USER = 0

#Robert's phone:
ACC_SID = "AC28c8c4fb97d6e0949e2ce45135ad2c9c"
AUTH_TOKEN = "c55558a79a700c94d537b33d63fe85c6"
FROM = "+18604312585"
BODY = "YOUR BABY MIGHT BE IN DANGER! CHECK YOUR CAR!"

#George's phone:
ACC_SID1 = "ACd03777f4973c4f1ffc3efed677cc57b1"
AUTH_TOKEN1 = "b22f0d66110237b42ebf63ccd2b4241e"
FROM1 = "+18482088916"

#Indicator
IN = 0

def user_is_bad():
	#Threading delay between 2 messages going to be 4 minutes
	threading.Timer(30.0, user_is_bad).start()
	send_message()

def send_message():
	#This function will send the messages
	users = User.query.all()
	client = Client(ACC_SID, AUTH_TOKEN)
	client1 = Client(ACC_SID1, AUTH_TOKEN1)
	for user in users:
		print("Print flag:")
		print(user.flag)
		print(user.number)
		client.messages.create(to=user.number, from_=FROM, body=BODY)

def activate():
	global IN
	if IN == 0:
		user_is_bad()
		IN = 1

@app.route('/')
def index():
	activate()
	return render_template('landingpage.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/account', methods=['GET', 'POST'])
@login_required
def private_route():
	form = AddContactForm(request.form)
	user = User.query.filter_by(id=session['user_id']).first()
	user.flag = 0
	db.session.commit()
	if request.method == "POST":
		form = AddContactForm(request.form)
		if user.name is null:
			user.name = form.name.data
			user.phone = form.phone.data
		elif user.name1 is null:
			user.name1 = form.name.data
			user.phone1 = form.phone.data
		elif user.name2 is null:
			user.name2 = form.name.data
			user.phone2 = form.phone.data
		db.session.commit()   
	return render_template('private.html', user=user, form=form)

'''@app.route('/add-contact', methods=['GET', 'POST'])
@login_required
def add_contact():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
	user = User.query.filter_by(id=session['user_id']).first()
    user.name = newtitle
    db.session.commit()
    return redirect("/")'''

@app.route('/test')
@login_required
def check():
	user = User.query.filter_by(username=session['name']).first()
	user.flag = 1
	db.session.commit()