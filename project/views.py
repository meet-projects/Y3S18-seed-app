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

@app.route('/price',)
def price():
	teachers=db.session.query(Teacher).order_by("cost desc").all()
	return render_template('feed.html', teachers=teachers)

@app.route('/signup')
def signup():
	return render_template('login_signup.html')

@app.route('/profile_edit')
@login_required
def private_route():
    return render_template('edit_profile_template.html')
