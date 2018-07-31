from flask import render_template, request, Flask, session, redirect, url_for
from flask import session as login_session
from flask_login import login_required
from . import app, db

from project.models import Journey, User, Ratings

@app.route('/browse')
def browse():
	all_journeys = Journey.query.all()

	print(session)
	if 'user_id' in session:
		user_id = session['user_id']
		current_user = User.query.filter_by(id=user_id).first()
		logged_in = True
		print(logged_in)
	else:
		logged_in = False
		current_user = 'Not Logged In'
	return render_template('browse.html', all_journeys=all_journeys, logged_in=logged_in, current_user=current_user)


@app.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
	if 'user_id' in session:
		user_id = session['user_id']
		current_user = User.query.filter_by(id=user_id).first()
		logged_in = True
	else:
		logged_in =  False
	user_id = session['user_id']
	user = User.query.filter_by(id=user_id).first()
	print(user.name)
	user_info = User.query.filter_by(id=request.form.get('user_id')).first()
	if request.method=='POST':
		user_info.country = request.form.get('country')
		user_info.profession = request.form.get('profession')
		user_info.birthday = request.form.get('birthday')
		user_info.city = request.form.get('city')
		user_info.number = request.form.get('number')
		user_info.is_storyteller = True
		db.session.add(user_info)
		db.session.commit()
		return render_template('st_profile.html', current_user=user, user=user_info, is_user=True, logged_in=logged_in)
	else:
		if user.is_storyteller==True:
			return render_template('st_profile.html', current_user=user, user=user_info, is_user=True, logged_in=logged_in) 
		else:
			return render_template('apply.html', current_user=user, logged_in=logged_in)


@app.route('/profile/<int:user_id>')
def profile(user_id):
	user = User.query.filter_by(id=user_id).first()
	if 'user_id' in session: #If there is a user logged in
		logged_in = True
		current_user = User.query.filter_by(id=user_id).first()
		current_user_id = session['user_id']
		current_user = User.query.filter_by(id=current_user_id).first()
		if user.id == current_user.id:
			is_user=True
		else:
			is_user=False
	else:
		current_user = 'Not Logged In'
		logged_in = False
		is_user = False
	if user.is_storyteller==True:
		st_journeys = Journey.query.filter_by(creator_id=user_id).all()
		return render_template('st_profile.html', user=user, is_user=is_user, current_user=current_user,st_journeys=st_journeys, is_storyteller=True, logged_in=logged_in)
	else:
		return render_template('profile.html',user=user, is_user=is_user, current_user=current_user, is_storyteller=False, logged_in=logged_in)




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


@app.route('/ratings/<int:journey_id>', methods=['GET','POST'])
@login_required
def add_rating(journey_id):
	current_user_id = session['user_id']
	current_user = User.query.filter_by(id=current_user_id).first()
	journey = Journey.query.filter_by(id=journey_id).first()
	all_ratings = Ratings.query.filter_by(journey_id=journey_id).all()
	creator_id= journey.creator_id
	creator= User.query.filter_by(id=creator_id).first()
	print(request.method)
	if request.method=="POST":
		new_rating = Ratings()
		new_rating.journey_id = journey_id
		new_rating.user = current_user.name
		new_rating.stars = request.form.get('stars')
		new_rating.title =  request.form.get('title')
		new_rating.review = request.form.get('review')
		print('111111111', new_rating.review)
		db.session.add(new_rating)
		db.session.commit() # I had a bug with this line. The problem was that I did "new_rating.user = current_user" and current_user in an object, but in the DB it is defined as a String.
		return render_template('journey.html', current_user=current_user, logged_in=True, all_ratings=all_ratings, journey=journey, creator=creator)
	else:
		return redirect('journey.html')
		#return render_template('journey.html', current_user=current_user, logged_in=True, all_ratings=all_ratings, journey=journey, creator=creator)	






if __name__ == "__main__":
	app.run()
