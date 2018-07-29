from flask import render_template, request, session
from flask_login import login_required
from project.models import *
from . import app


#@app.route('/')
#def index():
  #  return render_template('index.html')

@app.route('/feed')
@login_required
def feed():
	u = User.query.filter_by(id=session['user_id']).first()
	# print(request.__dict__)
	posts = Post.query.all()
	return render_template('feed.html', user=u, posts = posts)


@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')
