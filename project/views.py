from flask import render_template, request, Flask
from flask_login import login_required
from . import app, db

from project.models import Journey

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/private')
@login_required
def private_route():
	return render_template('private.html')


@app.route('/apply', methods=['GET', 'POST'])
def apply():
	if request.method=='POST':
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
		db.session.add(new_journey)
		db.session.commit()
		return render_template('journey_table_test.html', journey=new_journey)
	else:
		return render_template('apply.html')

@app.route('/journeys/<int:journey_id>')
def display_journey(journey_id):
        journey = Journey.query.filter_by(id=journey_id).first()
        creator = User.query.filter_by( id=journey.creator_id).first()
        return render_template('journey.html', journey=journey, creator= creator)



if __name__ == "__main__":
	app.run()
