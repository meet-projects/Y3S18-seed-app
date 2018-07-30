from flask import render_template, session
from flask_login import login_required

from project import db
from project.models import User,Teacher,Request
from . import app
from sqlalchemy import desc,asc

import sys, math

@app.route('/')
def index():
	return render_template('index.html')

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

@app.route('/feed/<int:pagenum>')
def feed_num(pagenum):
	all_teachers = db.session.query(Teacher).order_by("id desc").all()
	teachers = []
	pages = math.ceil(len(all_teachers)/4)
	if len(all_teachers)>=4*pagenum:
		for t in range(4*(pagenum-1),pagenum*4):
			teachers.append(all_teachers[t])
	else:
		for x in range(4*(pagenum-1),len(all_teachers)-1):
			teachers.append(all_teachers[x])
	for t in range(4*(pagenum-1),pagenum*4):
		teachers.append(t)
	print(pages)
	return render_template('feed.html', teachers=teachers,pages=pages)

@app.route('/sort/<sorting>',)
def price_sort(sorting):
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
	teachers=db.session.query(Teacher).filter_by(area="Galil Elion").all()
	return render_template('feed.html', teachers=teachers)

'''@app.route('/galil_tahton')
def galil_tahton():
	teachers=db.session.query(Teacher).filter_by(area="Galil Tahton").all()
	return render_template('feed.html', teachers=teachers)


@app.route('/hof_hagalil')
def hof_hagalil():
	teachers=db.session.query(Teacher).filter_by(area="Hof Hagalil").all()
	return render_template('feed.html', teachers=teachers)


@app.route('/golan')
def golan():
	teachers=db.session.query(Teacher).filter_by(area="Golan").all()
	return render_template('feed.html', teachers=teachers)


@app.route('/carmel')
def carmel():
	teachers=db.session.query(Teacher).filter_by(area="Carmel").all()
	return render_template('feed.html', teachers=teachers)

@app.route('/sharon')
def sharon():
	teachers=db.session.query(Teacher).filter_by(area="Sharon").all()
	return render_template('feed.html', teachers=teachers)

@app.route('/emek_israel')
def emek_israel():
	teachers=db.session.query(Teacher).filter_by(area="Emek Israel").all()
	return render_template('feed.html', teachers=teachers)


@app.route('/beit_shean')
def beit_shean():
	teachers=db.session.query(Teacher).filter_by(area="Beit Shean").all()
	return render_template('feed.html', teachers=teachers)


@app.route('/mishor_hakhof')
def mishor_hakhof():
	teachers=db.session.query(Teacher).filter_by(area="Mishor Hakhof").all()
	return render_template('feed.html', teachers=teachers)

@app.route('/jerusalem_district')
def jerusalem_district():
	teachers=db.session.query(Teacher).filter_by(area="Jerusalem District").all()
	return render_template('feed.html', teachers=teachers)


@app.route('/negev')
def negev():
	teachers=db.session.query(Teacher).filter_by(area="Negev").all()
	return render_template('feed.html', teachers=teachers)


@app.route('/shfelat_yehuda')
def shfelat_yehuda():
	teachers=db.session.query(Teacher).filter_by(area="Shfelat Yehuda").all()
	return render_template('feed.html', teachers=teachers)

@app.route('/judea_district')
def judea_district():
	teachers=db.session.query(Teacher).filter_by(area="Judea District").all()
	return render_template('feed.html', teachers=teachers)



@app.route('/west_bank')
def west_bank():
	teachers=db.session.query(Teacher).filter_by(area="West Bank").all()
	return render_template('feed.html', teachers=teachers)

@app.route('/arava')
def arava():
	teachers=db.session.query(Teacher).filter_by(area="arava").all()
	return render_template('feed.html', teachers=teachers)'''



@app.route('/lang/<language>')
def language_filter(language):
	print(language, file=sys.stdout)
	all_teachers=db.session.query(Teacher).all()
	print(all_teachers)
	teachers = []
	for t in all_teachers:
		print(t.name)
		if t.languages != None:
			l = t.languages.split(" ")
		else:
			l = []
		print(l.count(language.capitalize()))
		if l.count(language.capitalize()) > 0:
			print(l.count(language.capitalize()))
			print(t.languages)
			teachers.append(t)
	return render_template('feed.html', teachers=teachers)

'''@app.route('/english')
def english():
	all_teachers=db.session.query(Teacher).all()
	teachers = []
	for t in all_teachers:
		l = t.languages.split(" ")
		if l.count("English") > 0:
			teachers.append(t)
	return render_template('feed.html', teachers=teachers)

@app.route('/hebrew')
def hebrew():
	all_teachers=db.session.query(Teacher).all()
	teachers = []
	for t in all_teachers:
		l = t.languages.split(" ")
		if l.count("Arabic") > 0:
			teachers.append(t)
	return render_template('feed.html', teachers=teachers)'''


@app.route('/profile_template')
@login_required
def profile_template():
	teacher_id = session['user_id']
	user=User.query.filter_by(id=teacher_id).first()
	teacher2=Teacher.query.filter_by(user_id=teacher_id).first()
	this_teach_id=teacher2.id
	this_teach_books=Booking.query.filter_by(teacher_id=this_teach_id).all()
	return render_template('profile_template.html',teacher=teacher2,bookings=this_teach_books,user=user)


@app.route('/profile/<int:teacher_id>')
def profile(teacher_id):
	this_teach=Teacher.query.filter_by(id=teacher_id).first()
	return render_template('small_profile.html', teacher=this_teach)

@app.route('/<int:teacher_id>/edit_profile')
def edit_profile(teacher_id):
	teach=Teacher.query.filter_by(id=teacher_id).first()
	return render_template('edit_profile_template.html',teacher=teach)


