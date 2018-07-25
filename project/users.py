from flask import (
        Blueprint, redirect, render_template,
        Response, request, url_for
)
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError

from project import db
from project.forms import RegisterForm, LoginForm
from project.models import User,Teacher,Booking


users_bp = Blueprint('users', __name__)


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is None:
            user=User(username,password)
        login_user(user, remember=True)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('private_route')
        return redirect(next_page)
    else:
        return Response("<p>invalid form</p>")

    return render_template('register.html', form=form)
                

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user is None or not user.check_password(password):
                return Response("<p>Incorrect username or password</p>")
            login_user(user, remember=True)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('private_route')
            return redirect(next_page)
        else:
            return Response("<p>invalid form</p>")
    return render_template('login.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return Response("<p>Logged out</p>")

@users_bp.route('/teacher/<int:teacher_id>')
def profile(teacher_id):
    teacher = Teacher.query.filter_by(id=teacher_id).first()
    return render_template('profile_template.html', teacher=teacher)

@users_bp.route('/booking/<int:teacher_id>')
def booking(teacher_id):
    teacher = db.session.query(Teacher).filter_by(id=teacher_id).first()
    return render_template('booking.html', teacher=teacher)