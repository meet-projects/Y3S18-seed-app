from flask import render_template, request, session
from flask_login import login_required
from project.models import *
from . import app
from project.forms import AddArtForm	


@app.route('/feed')
@login_required
def feed():
    print("Hello World")
    form = AddArtForm(request.form)
    u = User.query.filter_by(id=session['user_id']).first()
    # print(request.__dict__)
    posts = Post.query.all()
    return render_template('feed.html', user=u, posts = posts, form = form)


@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')


@app.route('/profile',methods=['GET','POST'])
def profile():
    profileID = session['user_id']
    user = User.query.filter_by(id = profileID).first()
    posts = Post.query.filter_by(AuthorID = profileID).first()
    return render_template('profile.html', user = user, posts = posts)


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')



