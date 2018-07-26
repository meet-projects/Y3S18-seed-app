from flask import (
        Blueprint, redirect, render_template,
        Response, request, url_for , session
        )
from project import db

post_bp =  Blueprint('post', __name__)
@post_bp.route('/post', methods= ['GET', 'POST'])
def post():
	authorID = session['user_id']
	form = PostForm(request.form)
    if request.method == 'POST':
        print(form.validate_on_submit())
        if form.validate_on_submit():
            title = form.title.data
            text = form.text.data
            post = Post(authorID, title, text)    
            db.session.add(Post)
            db.session.commit()
            return render_template('index.html')    
        else:
            return Response("<p>invalid form</p>")
    return render_template('register.html', form=form)