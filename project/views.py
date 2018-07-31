from flask import render_template, request, session
from flask_login import login_required
from project.models import *
from . import app
#from project.forms import AddArtForm	


@app.route('/feed')
@login_required
def feed():
	return "hello world"
	form = AddArtForm(request.form)
	u = User.query.filter_by(id=session['user_id']).first()
	posts = Post.query.all()
	print(len(posts))
	return render_template('feed.html', user=u, posts = posts, form=form)


@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')
