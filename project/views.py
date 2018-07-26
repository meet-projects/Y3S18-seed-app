from flask import render_template, request, session
from flask_login import login_required
from project.models import User
from . import app


#@app.route('/')
#def index():
  #  return render_template('index.html')

@app.route('/feed')
@login_required
def feed():
	u = User.query.filter_by(id=session['user_id']).first()
	# print(request.__dict__)
	return render_template('index.html', user=u)


@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')
