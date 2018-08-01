from flask import render_template, request, Flask, session, redirect, url_for
from flask import session as login_session
from flask_login import login_required, current_user
from . import app, db
import time

from project.models import Journey, User, Ratings, Notification

########################################

############################################


@app.route('/browse')
@login_required
def browse():
	all_journeys = Journey.query.all()
	return render_template('browse.html', all_journeys=all_journeys)


@app.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
	if request.method=='POST':
		current_user.country    	= request.form.get('country')
		current_user.profession 	= request.form.get('profession')
		current_user.birthday   	= request.form.get('birthday')
		current_user.city      		= request.form.get('city')
		current_user.number         = request.form.get('number')
		current_user.is_storyteller = True
		db.session.commit()
		return redirect(url_for('profile', user_id=current_user))
	else:
		if current_user.is_storyteller==True:
			return redirect(url_for('profile', user_id=current_user.id))
		else:
			return render_template('apply.html')

@app.route('/profile/<int:user_id>')
def profile(user_id):
	profile = User.query.filter_by(id=user_id).first()
	if profile.is_storyteller==True:
		st_journeys = Journey.query.filter_by(creator_id=user_id).all()
		return render_template('st_profile.html',st_journeys=st_journeys, profile=profile)
	else:
		return render_template('profile.html', profile=profile)




@app.route('/add_journey', methods=['GET', 'POST'])
@login_required
def add_journey():
	if 'user_id' in session:
		user_id = session['user_id']
		current_user = User.query.filter_by(id=user_id).first()
		logged_in = True
	else:
		logged_in =  False
	user_id = session['user_id']
	user = User.query.filter_by(id=user_id).first()
	if request.method=='POST':
		new_journey = Journey()
		new_journey.creator_id = request.form.get('user_id')
		print('session user id--->', user_id)
		print('request form user id --->', request.form.get('user_id'))
		new_journey.title = request.form.get('title')
		new_journey.description = request.form.get('description')
		new_journey.location  = request.form.get('location')
		new_journey.duration  = request.form.get('duration')
		new_journey.category  = request.form.get('category')
		new_journey.requirements  = request.form.get('requirements')
		new_journey.people_range  = request.form.get('people_range')
		new_journey.price  = request.form.get('price')
		new_journey.picture  = request.form.get('picture')
		db.session.add(new_journey)
		db.session.commit()
		return render_template('journey.html', journey=new_journey, current_user=user, creator=user, logged_in=logged_in)
	else:
		return render_template('add_journey.html', current_user=user, logged_in=logged_in)






@app.route('/journeys/<int:journey_id>')
def display_journey(journey_id):
	print('0000000000000000000000')
	if 'user_id' in session:
		user_id = session['user_id']
		current_user = User.query.filter_by(id=user_id).first()
		logged_in = True
	else:
		logged_in =  False
	journey = Journey.query.filter_by(id=journey_id).first()
	creator = User.query.filter_by(id=journey.creator_id).first()
	all_ratings = Ratings.query.filter_by(journey_id=journey_id).all()
	print('creator ---->', creator)
	return render_template('journey.html', journey=journey, creator=creator, logged_in=logged_in, all_ratings=all_ratings)

@app.route('/im_interested/<int:interested_user_id>/<int:journey_id>/<int:st_id>', methods=['GET','POST'])
def im_interested(interested_user_id, journey_id, st_id):
	print('1111111111111111111', request.method)
	current_user_id = session['user_id']
	current_user = User.query.filter_by(id=current_user_id).first()
	if request.method == 'POST':
		new_notification = Notification()
		new_notification.st_id = st_id
		new_notification.journey_id = journey_id
		new_notification.interested_user_id = interested_user_id
		interested_user = User.query.filter_by(id=interested_user_id).first()
		new_notification.interested_user_name = interested_user.name
		journey = Journey.query.filter_by(id=journey_id).first()
		new_notification.journey_title = journey.title
		db.session.add(new_notification)
		db.session.commit()
		all_journeys = Journey.query.all()
		return render_template('browse.html', current_user= current_user, logged_in=True, all_journeys=all_journeys)



@app.route('/ratings/<int:journey_id>', methods=['GET','POST'])
@login_required
def add_rating(journey_id):
	current_user_id = session['user_id']
	current_user = User.query.filter_by(id=current_user_id).first()
	journey = Journey.query.filter_by(id=journey_id).first()
	all_ratings = Ratings.query.filter_by(journey_id=journey_id).all()
	creator_id = journey.creator_id
	creator = User.query.filter_by(id=creator_id).first()
	print(request.method)
	if request.method == "POST":
		new_rating = Ratings()
		new_rating.journey_id = journey_id
		new_rating.user = current_user.name
		new_rating.stars = request.form.get('stars')
		new_rating.title =  request.form.get('title')
		new_rating.review = request.form.get('review')
		localtime = time.localtime(time.time())
		new_rating.time = str(localtime[1])+"/"+str(localtime[2])+"/"+str(localtime[0])+" at "+str(localtime[3])+":"+str(localtime[4])
		db.session.add(new_rating)
		db.session.commit() # I had a bug with this line. The problem was that I did "new_rating.user = current_user" and current_user in an object, but in the DB it is defined as a String.
		return render_template('journey.html', current_user=current_user, logged_in=True, all_ratings=all_ratings, journey=journey, creator=creator)
	else:
		return redirect('journey.html')
		#return render_template('journey.html', current_user=current_user, logged_in=True, all_ratings=all_ratings, journey=journey, creator=creator)	


@app.route('/notification/<int:st_id>', methods=['GET'])
@login_required
def display_notifications(st_id):
	if request.method == 'GET':
		current_user_id = session['user_id']
		current_user = User.query.filter_by(id=current_user_id).first()
		all_notifications = Notification.query.filter_by(st_id=st_id)
		return render_template('notifications.html', all_notifications=all_notifications, logged_in=True, current_user=current_user)




if __name__ == "__main__":
	app.run()
