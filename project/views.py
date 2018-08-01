from flask import render_template, request, session
from flask_login import login_required
from project.models import *
from . import app
from project.forms import AddArtForm    

@app.route('/feed')
@login_required
def feed():
    form = AddArtForm(request.form)
    u = User.query.filter_by(id=session['user_id']).first()
    posts = Post.query.filter_by(ArtURL = '').all()
    return render_template('feed.html', user=u, posts = posts, form = form)

@app.route('/main111')
@login_required
def main():
    print("Hello World")
    form = AddArtForm(request.form)
    u = User.query.filter_by(id=session['user_id']).first()
    posts = Post.query.filter(Post.ArtURL != '').all()
    return render_template('mainfeed.html', user=u, posts = posts, form = form)


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

    #posts = Post.query.filter_by(AuthorID = profileID).first()
    #return render_template('profile.html', user = user, posts = posts)


@app.route('/viewstory/<int:PostID>', methods = ['GET','POST'])
def view_story(PostID):
    form = AddArtForm(request.form)
    post = Post.query.filter_by(id = PostID).first()
    return render_template('viewstory.html', post = post, form = form)
