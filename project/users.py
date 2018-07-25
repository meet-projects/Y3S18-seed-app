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
    #form = RegisterForm(request.form)

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('psw')
        password2= request.form.get('psw-repeat')
        name= request.form.get('name')
        city=request.form.get('city')
        fee=request.form.get('fee')
        description=request.form.get('description')
        area=request.form.get('area')
        phonenum=request.form.get('phonenum')
        car_type=request.form.get('car_type')
        license_num=request.form.get('license_num')
        languages="to be filled"
        if password== password2:
            user = User.query.filter_by(email=email).first()
            if user is None:
                user=User(email,password)
                user.email = email
                user.password_hash = password
                user_id = user.id
                teacher=Teacher(user_id,name,area,city,description,fee,phonenum,"http://i.imgur.com/hfH9CiC.png",car_type,license_num)
                db.session.add(user)
                db.session.add(teacher)
                db.session.commit()
            login_user(user, remember=True)
            return redirect('profile_template')
            ##next_page = request.args.get('next')
            ##if not next_page or url_parse(next_page).netloc != '':
               ## next_page = url_for('private_route')
            ##return redirect(next_page)
        else:
            return Response("<p>invalid form</p>")

    return render_template('login_signup.html', form=form)
                

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            email = email = request.form.get('email')
            password = email = request.form.get('password')
            user = User.query.filter_by(email=email).first()
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
    teacher = db.session.query().filter_by(id=teacher_id).first()
    return render_template('profile_template.html', teacher=teacher)

@users_bp.route('/booking/<int:teacher_id>')
def booking(teacher_id):
    teacher = db.session.query(Teacher).filter_by(id=teacher_id).first()
    return render_template('booking.html', teacher=teacher)