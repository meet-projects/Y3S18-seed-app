from flask import (
        Blueprint, redirect, render_template,
        Response, request, url_for , session,
        abort
)
from flask_login import login_required, current_user
from project.models import User, Post, Like
from . import app
from project.forms import AddArtForm    


@app.route('/feed', methods=['POST','GET'])
@login_required
def feed():
    posts = Post.query.filter(Post.ArtURL != '').all()
    return render_template('mainfeed.html', posts=posts)


@app.route('/profile')
@login_required
def my_profile():
    username = current_user.username
    return redirect("/profiles/" + username)


@app.route('/profiles/<username>')
@login_required
def profile(username):
    print(username + "<<<<<<<<<<<<<<<<<<<")
    visited_user = User.query.filter_by(username=username).first()
    art = Post.query.filter_by(ArtistID = visited_user.id)
    if visited_user:
        return render_template('profile.html', visited_user=visited_user, art_pieces = art)
    else:
        return abort(404)

@app.route('/inspiration')
@login_required
def stories():
    posts = Post.query.filter_by(ArtURL = '').all()
    return render_template('stories.html', posts=posts)

@app.route('/landingpage')
def landingpage():
        return render_template('landingpage.html')    

#read more function and add art
@app.route('/stories/<int:post_id>', methods = ['GET','POST'])
@login_required
def list_detail_stories(post_id):
    form = AddArtForm(request.form)    
    post = Post.query.filter_by(id = post_id).first()
    if (post.ArtURL != ''):
        artist = User.query.filter_by(id = post.ArtistID).first()
        return render_template('viewstory.html', post=post, form=form, user = artist)
    else:
        return render_template('viewstory.html', post=post, form=form)
