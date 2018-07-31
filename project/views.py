from flask import render_template, request, session
from flask_login import login_required
from project.models import *
from . import app

@app.route('/feed')
@login_required
def feed(username = None):
    print("Hello World")
    u = User.query.filter_by(id=session['user_id']).first()
    posts = Post.query.all()
    return render_template('feed.html', user=u, posts = posts)


@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')

@app.route('/profile', defaults={'username':None})
@app.route('/profile/<username>',methods=['GET','POST'])
@login_required
def profile(username = None):
    profileID = session['user_id']
    if username is None:
        username = User.query.filter_by(id = profileID).first().username
    visitedID = User.query.filter_by(username = username).first().id
    user = User.query.filter_by(id = profileID).first()
    return render_template('profile.html', user = user, my_profile = (profileID == visitedID))
