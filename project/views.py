from flask import render_template
from flask_login import login_required

from project import db
from project.models import User,Teacher,Booking
from . import app
from sqlalchemy import desc

@app.route('/')
def feed():
	# teachers = db.session.query(Teacher).all()
	teachers = Teacher.query.all()
	print(teachers)
	return render_template('feed.html', teachers=teachers)

@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')
