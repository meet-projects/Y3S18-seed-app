from flask import render_template, request, session
from flask_login import login_required
from project.models import *
from . import app
#from project.forms import AddArtForm	


@app.route('/feed')
@login_required
def feed():
<<<<<<< HEAD
	return "hello world"
	form = AddArtForm(request.form)
	u = User.query.filter_by(id=session['user_id']).first()
	posts = Post.query.all()
	print(len(posts))
	return render_template('feed.html', user=u, posts = posts, form=form)
=======
    print("Hello World")
    u = User.query.filter_by(id=session['user_id']).first()
    # print(request.__dict__)
    posts = Post.query.all()
    return render_template('feed.html', user=u, posts = posts)
>>>>>>> b232ab3a152119d9096c7aa1b16cb165b3ecf488


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
