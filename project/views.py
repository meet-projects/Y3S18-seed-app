from flask import render_template, request, Flask, session, redirect, url_for
from flask import session as login_session
from flask_login import login_required
from . import app, db

from project.models import Journey, User

@app.route('/')
def browse():
	user_id = session['user_id']
	current_user = User.query.filter_by(id=user_id).first()
	# WHAT ZAIN DID ===>  all_journeys = db.session.query(Journey).all()
	all_journeys = Journey.query.all()
	return render_template('browse.html', all_journeys=all_journeys, current_user=current_user)
	# we need to now how to filter 


@app.route('/private')
@login_required
def private_route():
	return render_template('private.html')


@app.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
	# global current_user
	# print(current_user)
	user_id = session['user_id']
	user = User.query.filter_by(id=user_id).first()
	print(user.name)
	if request.method=='POST':
		user_info = User.query.filter_by(id=request.form.get('user_id')).first()
		user_info.country = request.form.get('country')
		user_info.profession = request.form.get('profession')
		user_info.birthday = request.form.get('birthday')
		user_info.city = request.form.get('city')
		user_info.number = request.form.get('number')
		db.session.add(user_info)
		db.session.commit()
		
		################# JOURNEY TABLE ###################
		new_journey = Journey()
		new_journey.creator_id = request.form.get('user_id')
		new_journey.title = request.form.get('title')
		new_journey.description = request.form.get('description')
		new_journey.location  = request.form.get('location')
		new_journey.duration  = request.form.get('duration')
		new_journey.category  = request.form.get('category')
		new_journey.requirements  = request.form.get('requirements')
		new_journey.people_range  = request.form.get('people_range')
		new_journey.price  = request.form.get('price')
		new_journey.picture  = request.form.get('picture')
		print(new_journey.description)
		db.session.add(new_journey)
		db.session.commit()
		return render_template('journey.html', journey=new_journey, current_user=user, creator=user_info)
	else:
		print('hereeee')
		return render_template('apply.html', current_user=user)

@app.route('/journeys/<int:journey_id>')
def display_journey(journey_id):
        journey = Journey.query.filter_by(id=journey_id).first()
        creator = User.query.filter_by(id=journey.creator_id).first()
        print('creator ---->', creator)
        return render_template('journey.html', journey=journey, creator=creator)

@app.route('/profile/<user_id>')
def profile(user_id):
	user=User.query.filter_by (id=user_id).first()
	is_user=False
	user_id = session['user_id']
	current_user = User.query.filter_by(id=user_id).first()
	if user.id==current_user.id:
	 	is_user=True
	return render_template('profile.html',user=user, is_user=is_user, current_user=current_user)



if __name__ == "__main__":
	app.run()
