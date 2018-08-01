from flask import render_template, request, session
from flask_login import login_required, current_user
from project.models import User, Post, Like
from . import app
from project.forms import AddArtForm    


@app.route('/feed', methods=['POST','GET'])
@login_required
def feed():
    posts = Post.query.filter(Post.ArtURL != '').all()
    return render_template('mainfeed.html', posts=posts)

@app.route('/profiles/<username>')
@login_required
def profile(username):
    visiting_user = User.query.filter_by(username=username)
    return render_template('profile.html', visiting_user=visiting_user)


#read more function and add art
@app.route('/stories/<int:post_id>', methods = ['GET','POST'])
@login_required
def list_detail_stories(post_id):
    if post_id:
        form = AddArtForm(request.form)
        post = Post.query.filter_by(id = post_id).first()
        return render_template('viewstory.html', post=post, form=form)
    else:
        posts = Post.query.filter_by(ArtURL = '').all()
        return render_template('stories.html', posts=posts)