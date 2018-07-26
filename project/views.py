from flask import render_template, request, session
from flask_login import login_required
from project import db
from project.models import User

import os
from twilio.rest import Client
import threading

from . import app

NEED = 0

ACC_SID = "AC28c8c4fb97d6e0949e2ce45135ad2c9c"
AUTH_TOKEN = "c55558a79a700c94d537b33d63fe85c6"
FROM = "+18604312585"
BODY = "YOUR BABY MIGHT BE IN DANGER! CHECK YOUR CAR!"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/private', methods=['GET', 'POST'])
@login_required
def private_route():
	global NEED
	NEED = 0
	if request.method == 'POST':
		user = User.query.filter_by(id=session['user_id']).first()

		client = Client(ACC_SID, AUTH_TOKEN)

		client.messages.create(to=user.number, from_=FROM, body=BODY) 

		NEED = 1

		user_is_bad()

		return render_template('check.html')

	return render_template('private.html')

def user_is_bad():
	global NEED
	user = User.query.filter_by(id=session['user_id']).first()
	client = Client(ACC_SID, AUTH_TOKEN)
	threading.Timer(30.0, user_is_bad).start()
	print(NEED)
	if NEED == 1:
		client.messages.create(to=user.number, from_=FROM, body=BODY)
		NEED = 1  