from flask import render_template, session
from flask_login import login_required, current_user

from project import db
from project.models import User,Teacher,Request, City
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
	all_cities = City.query.all()
	#teachers = []
	#pages = int(math.ceil(len(all_teachers)/4))
	#if len(all_teachers)>=4:
	#	for t in range(0,4):
	#		teachers.append(all_teachers[t])
	#else:
	#teachers = all_teachers

	return render_template('feed.html', teachers=all_teachers, all_cities=all_cities ,page="All Instructors",results="",thing="")

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
	all_cities = City.query.all()
	teachers=[]
	if sorting == "low":
		teachers=db.session.query(Teacher).order_by("cost asc").all()
	elif sorting == "high":
		teachers=db.session.query(Teacher).order_by("cost desc").all()

	return render_template('feed.html', teachers=teachers, all_cities=all_cities, page="Filtering by Price",results="",thing=sorting.capitalize())


@app.route('/lang/<language>')
def language_filter(language):
	all_cities = City.query.all()
	all_teachers=db.session.query(Teacher).all()
	teachers = []
	results=""
	for t in all_teachers:
		if t.languages != None:
			l = t.languages.split(" ")
		else:
			l = []
		if l.count(language.capitalize()) > 0:
			teachers.append(t)
	if len(teachers)==0:
		results="No Results"
	return render_template('feed.html', teachers=teachers, page="Filtering by Language",results=results, all_cities=all_cities,thing=language.capitalize())

@app.route('/city/<int:city>')
def city(city):
	all_cities = City.query.all()
	all_teachers = Teacher.query.all()
	teachers = []
	results=""
	for t in all_teachers:
		if t.city == City.query.filter_by(id=city).first().city:
			teachers.append(t)

	if len(teachers)==0:
		results="No Results"
	cityname=City.query.filter_by(id=city).first().city
	return render_template('feed.html', teachers=teachers,page="Filtering by City", all_cities=all_cities,results=results,thing=cityname)

@app.route('/signup')
def signup():
	return render_template('register.html')

@app.route('/profile_template')
@login_required
def profile_template():
	t=Teacher.query.filter_by(user_id=current_user.id).first()
	this_teach_id=t.id
	all_cities = City.query.all()
	all_requests=Request.query.filter_by(teacher_id=t.id)
	return render_template('profile_template.html',teacher=t,user=current_user, all_cities=all_cities,requests=all_requests)


@app.route('/profile/<int:teacher_id>')
def profile(teacher_id):
	this_teach=Teacher.query.filter_by(id=teacher_id).first()
	return render_template('small_profile.html', teacher=this_teach)

@app.route('/<int:teacher_id>/edit_profile')
def edit_profile(teacher_id):
	teach = Teacher.query.filter_by(id=teacher_id).first()
	all_cities = City.query.all()
	return render_template('edit_profile_template.html', teacher=teach, all_cities=all_cities)
