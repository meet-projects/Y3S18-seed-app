from flask import (
        Blueprint, redirect, render_template,
        Response, request, url_for , session
        )
from flask_login import login_user, login_required, logout_user, current_user
from project import db
from project.forms import PostForm, AddArtForm
from project.models import Post, User


post_bp =  Blueprint('add_post', __name__)

@post_bp.route('/posts', methods= ['GET', 'POST'])
@login_required
def add_post():
    form = PostForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            text = form.text.data
            post = Post(current_user.id, title, text)    
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('feed'))   
        else:
            return render_template('add_post.html', form=form, error="An error occured")
    return render_template('add_post.html', form=form)

@post_bp.route('/add-art/<int:post_id>', methods= ['POST'])
@login_required
def add_art(post_id):
    form = AddArtForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            post = Post.query.filter_by(id = post_id).first()
            art_url = form.art_url.data
            post.ArtURL = art_url
            post.ArtistID = current_user.id
            db.session.commit()
            return redirect(url_for('feed'))   
        else:
            return Response("<p>invalid form</p>")












