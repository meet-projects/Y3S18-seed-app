from flask import render_template, session
from flask_login import login_required, current_user

from project import db
from project.models import *
from flask_login import login_user, login_required, logout_user, current_user
from . import app
from sqlalchemy import desc,asc

import sys, math


##catagories
@app.route('/feed')
@login_required
def feed():
	if current_user.account_type == "student":
		student = Student.query.filter_by(user_id = current_user.id).first()
		teachers = db.session.query(Teacher).all()
		all_teachers_tuples = []
		for i in teachers:
			matching = 0
			if student.city == i.city:
				matching+=5
			if i.cost>=student.min_price and i.cost<=student.max_price:
				matching+=1
			sgb = student.gearbox.split(" ")
			tgb = i.gearbox.split(" ")
			for g in sgb:
				if tgb.count(g)>0:
					matching+=(1/len(sgb))
			slang = student.languages.split(" ")
			tlang = i.languages.split(" ")
			for l in slang:
				if tlang.count(l)>0:
					matching+=(1/len(slang))
			all_teachers_tuples.append((matching,i.id))

		all_teachers_tuples.sort(reverse=True)
		all_teachers = []
		
		for i in all_teachers_tuples:

			all_teachers.append(Teacher.query.filter_by(id=i[1]).first())


		all_cities = City.query.all()
	#teachers = []
	#pages = int(math.ceil(len(all_teachers)/4))
	#if len(all_teachers)>=4:
	#	for t in range(0,4):
	#		teachers.append(all_teachers[t])
	#else:
	#teachers = all_teachers

		return render_template('feed.html', teachers=all_teachers, all_cities=all_cities ,page="Your customized feed",results="",thing="Your best matches are first!")
	else:
		ts=Teacher.query.all()
		cities=City.query.all()
		return render_template('feed.html',teachers=ts,all_cities=cities,page="All Instructors",results="",thing="")

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




#teachers


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




@app.route('/<int:teacher_id>/edit_profile')
def edit_profile(teacher_id):
	teach = Teacher.query.filter_by(id=teacher_id).first()
	all_cities = City.query.all()
	user=User.query.filter_by(id=teach.user_id).first()
	return render_template('edit_profile_template.html', teacher=teach, all_cities=all_cities)


@app.route('/student_info/<int:st_id>')
def student_info(st_id):
	this_student=Student.query.filter_by(id=st_id).first()
	done=Request.query.filter_by(student_id=this_student.id).first().done
	return render_template('student_info.html',student=this_student,done=True)




##students

@app.route('/studentsignup')
def studentsignup():
	return render_template('stu_signup.html')

@app.route('/filters')
def filters():
	all_cities = City.query.all()
	return render_template('filter.html',all_cities=all_cities)

##@app.route('/student_edit_profile/<int:student_id>')
##def student_edit_profile(student_id):
##	student = Student.query.filter_by(id=student_id).first()
##	all_cities = City.query.all()

##	return render_template('filter_modal.html', student=student, all_cities=all_cities)##

@app.route('/profile/<int:teacher_id>')
def profile(teacher_id):
	this_teach=Teacher.query.filter_by(id=teacher_id).first()
	user=User.query.filter_by(id=current_user.id).first()
	return render_template('small_profile.html', teacher=this_teach,current_user=user)