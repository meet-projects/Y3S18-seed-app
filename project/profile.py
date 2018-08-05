from flask import (
        Blueprint, redirect, render_template,
        Response, request, url_for , session,
        abort
)
from flask_login import login_required, current_user
from project import db
from project.models import User, Post, Like
from . import app
from project.forms import ProfilePicForm

profile_bp =  Blueprint('profile', __name__)

@profile_bp.route('/change_pic', methods= ['POST'])
@login_required
def change_pic():
    form = ProfilePicForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(id = current_user.id).first()
            user.profile_pic_url = form.profile_pic_url.data
            db.session.commit()
            return redirect(url_for('profile', username = current_user.username))   
        else:
            return Response("<p>invalid form</p>")