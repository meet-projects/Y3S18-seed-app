from flask import render_template
from flask_login import login_required

from . import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')


@app.route('/become-a-storyteller', methods=['GET', 'POST'])
def become_a_storyteller():
	if request.method=='POST':
		new_journey = Journey()
		new_journey.title = request.form.get('title')
		new_journey.description = request.form.get('description')
		new_journey.start_location  = request.form.get('start_location')
		new_journey.end_location  = request.form.get('end_location')
		new_journey.duration  = request.form.get('duration')
		new_journey.people_type  = request.form.get('people_type')
		new_journey.requirements  = request.form.get('requirements')
		db.session.add(new_journey)
		db.session.commit()
	else:
		return render_template('what_ade_called_it')



if __name__ == "__main__":
    app.run()
