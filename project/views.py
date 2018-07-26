from flask import render_template, request, Flask, session, redirect, url_for
from flask import session as login_session
from flask_login import login_required
from . import app, db

from project.models import Journey, User

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/private')
@login_required
def private_route():
	return render_template('private.html')


@app.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
	if request.method=='POST':
		user_info = User.query.filter_by(id=request.form.get('user_id')).first()
		#print(user_info)
		#print(request)
		#print(user_info.one())
		user_info.country = request.form.get('country')
		user_info.profession = request.form.get('profession')
		user_info.birthday = request.form.get('birthday')
		user_info.city = request.form.get('city')
		user_info.number = request.form.get('number')
		db.session.add(user_info)
		db.session.commit()
############################################### CONNECT THIS TO CURRENT USER ########################################################

		new_journey = Journey()
		#new_journey.creator_id = current_user.id
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
		return render_template('journey_table_test.html', journey=new_journey)
	else:
		return render_template('apply.html')





if __name__ == "__main__":
	app.run()
