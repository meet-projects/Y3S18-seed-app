from flask import render_template, session
from flask_login import login_required

from project import db
from project.models import User,Teacher,Request
from . import app
from sqlalchemy import desc,asc

import sys, math

##@app.route('/')
##def index():
##	loginform = LoginForm(request.form)
##	return render_template('index.html',loginform=loginform)

@app.route('/feed')
def feed():
	all_teachers = db.session.query(Teacher).order_by("id desc").all()
	#teachers = []
	#pages = int(math.ceil(len(all_teachers)/4))
	#if len(all_teachers)>=4:
	#	for t in range(0,4):
	#		teachers.append(all_teachers[t])
	#else:
	#teachers = all_teachers
	return render_template('feed.html', teachers=all_teachers)

##@app.route('/feed/<int:pagenum>')
##def feed_num(pagenum):
##	all_teachers = db.session.query(Teacher).order_by("id desc").all()
##	teachers = []
##	pages = math.ceil(len(all_teachers)/4)
##	if len(all_teachers)>=4*pagenum:
##		for t in range(4*(pagenum-1),pagenum*4):
##			teachers.append(all_teachers[t])
##	else:
##		for x in range(4*(pagenum-1),len(all_teachers)-1):
##			teachers.append(all_teachers[x])
##	for t in range(4*(pagenum-1),pagenum*4):
##		teachers.append(t)
##	print(pages)
##	return render_template('feed.html', teachers=teachers,pages=pages)

@app.route('/sort/<sorting>',)
def price_sort(sorting):
	teachers=[]
	if sorting == "low":
		teachers=db.session.query(Teacher).order_by("cost asc").all()
	elif sorting == "high":
		teachers=db.session.query(Teacher).order_by("cost desc").all()
	return render_template('feed.html', teachers=teachers)

'''@app.route('/hightolow',)
def hightolow():
	teachers=db.session.query(Teacher).order_by("cost desc").all()
	return render_template('feed.html', teachers=teachers)'''

@app.route('/<area>')
def area_filter(area):
	l = area.split("_")
	area = ""
	for w in l:
		w = w.capitalize()
		area = area+w
	teachers=db.session.query(Teacher).filter_by(city="area").all()
	return render_template('feed.html', teachers=teachers)



@app.route('/lang/<language>')
def language_filter(language):
	all_teachers=db.session.query(Teacher).all()
	teachers = []
	for t in all_teachers:
		if t.languages != None:
			l = t.languages.split(" ")
		else:
			l = []
		if l.count(language.capitalize()) > 0:
			teachers.append(t)
	return render_template('feed.html', teachers=teachers)

@app.route('/signup')
def signup():
	return render_template('register.html')

@app.route('/profile_template')
@login_required
def profile_template():
	teacher_id = session['user_id']
	user=User.query.filter_by(id=teacher_id).first()
	teacher2=Teacher.query.filter_by(user_id=teacher_id).first()
	this_teach_id=teacher2.id
	return render_template('profile_template.html',teacher=teacher2,user=user)


@app.route('/profile/<int:teacher_id>')
def profile(teacher_id):
	this_teach=Teacher.query.filter_by(id=teacher_id).first()
	return render_template('small_profile.html', teacher=this_teach)

@app.route('/<int:teacher_id>/edit_profile')
def edit_profile(teacher_id):
	teach=Teacher.query.filter_by(id=teacher_id).first()
	return render_template('edit_profile_template.html',teacher=teach)

@app.route('/test_feed')
def feed_test():
	return render_template('new_feed.html')