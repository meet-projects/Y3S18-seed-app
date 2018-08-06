from flask import (
		Blueprint, redirect, render_template,
		Response, request, url_for , session,
		abort
)
from flask_login import login_required, current_user
from project.models import User, Post, Like
from . import app
from project.forms import *   


@app.route('/feed', methods=['POST','GET'])
@login_required
def feed():
	posts = Post.query.filter(Post.ArtURL != '').all()
	return render_template('feed.html', posts=posts)


@app.route('/profile')
@login_required
def my_profile():
	username = current_user.username
	print(username)
	return redirect("/profiles/" + username)


@app.route('/profiles/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
	if username == "None":
		print("wtf")
	print(username + "<<<<<<<<<<<<<<<<<<<")
	visited_user = User.query.filter_by(username=username).first()
	pic_form = ProfilePicForm(request.form)    
	bio_form = ProfileBioForm(request.form)  
	art_pieces = Post.query.filter_by(ArtistID = visited_user.id).all()
	art_len =  len(art_pieces)
	print(art_len)
	if (int(art_len)%3==0):
		amount_of_rows = int(art_len/3)
	else:
		amount_of_rows = int(art_len/3) +1
	print(amount_of_rows)
	if visited_user:
		print("visited user")
		return render_template('profile.html', visited_user=visited_user, pic_form = pic_form, bio_form = bio_form, art_pieces = art_pieces, amount_of_rows = amount_of_rows)
	else:
		return abort(404)


@app.route('/inspiration')
@login_required
def stories():
	posts = Post.query.filter_by(ArtURL = None).all()
	return render_template('feed.html', posts=posts, show = 'artless')

@app.route('/')
def landingpage():
	return render_template('landingpage.html')    
		

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


#read more function and add art
@app.route('/stories/<int:post_id>', methods = ['GET','POST'])
@login_required
def list_detail_stories(post_id):
	form = AddArtForm(request.form)    
	post = Post.query.filter_by(id = post_id).first()
	if (post.ArtURL != None):
		artist = User.query.filter_by(id = post.ArtistID).first()
		return render_template('viewstory.html', post=post, form=form, user = artist)
	else:
		return render_template('viewstory.html', post=post, form=form)
