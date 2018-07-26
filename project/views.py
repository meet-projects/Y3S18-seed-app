from flask import render_template, session
from flask_login import login_required

from project import db
from project.models import User,Teacher,Booking
from . import app
from sqlalchemy import desc

@app.route('/')
@app.route('/feed')
@app.route('/profile/feed')
def feed():
	teachers = db.session.query(Teacher).all()
	print(teachers)
	return render_template('feed.html', teachers=teachers)

@app.route('/lowtohigh',)
def lowtohigh():
	teachers=db.session.query(Teacher).order_by("cost desc").all()
	return render_template('feed.html', teachers=teachers)

@app.route('/hightolow',)
def hightolow():
	teachers=db.session.query(Teacher).order_by("cost desc").all()
	return render_template('feed.html', teachers=teachers)

@app.route('/galil_elion')
def galil_elion():
	teachers=db.session.query(Teacher).filter_by(area="Galil Elion").all()
	return render_template('feed.html', teachers=teachers)

@app.route('/galil_tahton')
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
	return render_template('feed.html', teachers=teachers)



@app.route('/arabic')
def arabic():
	all_teachers=db.session.query(Teacher).all()
	teachers = []
	for t in all_teachers:
		l = t.languages.split(" ")	
		if l.count("Arabic") > 0:
			teachers.append(t)
	return render_template('feed.html', teachers=teachers)

@app.route('/english')
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
	return render_template('feed.html', teachers=teachers)


@app.route('/profile_template')
@login_required
def profile_template():
	teacher_id = session['user_id']
	teacher2=Teacher.query.filter_by(user_id=teacher_id).first()
	this_teach_id=teacher2.id
	this_teach_books=Booking.query.filter_by(teacher_id=this_teach_id).all()
	return render_template('profile_template.html',teacher=teacher2,bookings=this_teach_books)


@app.route('/profile/<int:teacher_id>')
def profile(teacher_id):
	this_teach=Teacher.query.filter_by(id=teacher_id).first()
	return render_template('small_profile.html', teacher=this_teach)

@app.route('/edit_profile')
def edit_profile():
	return render_template('edit_profile_template.html')


@app.route('/<int:teacher_id>/booking')
def booking(teacher_id):
	studentname=request.form.get('name')
	studentnum=request.form.get('num')
	thisteacher=Teacher.query.filter_by(id=teacher_id).first()
	book=Booking(studentname,studentnum,thisteacher.id,False)
	db.session.add(book)
	db.session.commit()
