from flask import (
		Blueprint, redirect, render_template,
		Response, request, url_for , session
		)
from flask_login import login_user, login_required, logout_user, current_user
from project import db
from project.forms import PostForm, AddArtForm
from project.models import Post, User


post_bp =  Blueprint('add_post', __name__)

@post_bp.route('/create_post', methods= ['GET', 'POST'])
@login_required
def add_post():
	form = PostForm(request.form)
	if request.method == 'POST':

		title = form.title.data
		text = form.text.data

		test_result = test_add_post(form)

		if test_result == "success":
			post = Post(current_user.id, title, text)
			db.session.add(post)
			db.session.commit()
			return redirect(url_for("feed"))
		else:
			data = {'err_msg':test_result}
			return render_template('add_post.html',form = form, data = data)

	else:
		return render_template('add_post.html', form=form)

def test_add_post(form):
	title = form.title.data
	text = form.text.data
	if not title or title == "":
		return "post has to have a title"
	if not text or text == "":
		return "post has to have text"
	return "success"

@post_bp.route('/add_art/<int:post_id>', methods= ['POST'])
@login_required
def add_art(post_id):
	form = AddArtForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			post = Post.query.filter_by(id = post_id).first()
			art_url = form.art_url.data
			post.ArtURL = art_url
			post.ArtistNotes = form.artist_notes.data
			post.ArtistID = current_user.id
			db.session.commit()
			return redirect(url_for('feed'))   
		else:
			return Response("<p>invalid form</p>")












