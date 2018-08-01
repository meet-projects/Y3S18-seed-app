from flask import render_template, request, session
from flask_login import login_required
from project.models import *
from . import app
from project.forms import AddArtForm	

@app.route('/feed', methods=['POST','GET'])
@login_required
def feed():
    print("Hello World")
    form = AddArtForm(request.form)
    u = User.query.filter_by(id=session['user_id']).first()
    posts = Post.query.all()
    return render_template('feed.html', user=u, posts = posts, form = form)


@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')

@app.route('/profiles/<username>',methods=['GET','POST'])
@login_required
def profile(username):
    profileID = session['user_id']
    visitedID = User.query.filter_by(username = username).first().id
    user = User.query.filter_by(id = profileID).first()
    return render_template('profile.html', user = user, my_profile = (profileID == visitedID))