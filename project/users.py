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
        languages="to be filled"
        if password== password2:
            user = User.query.filter_by(email=email).first()
            if user is None:
                user=User(email,password)
                teahcer=Teacher(user.user_id,name,area,city,description,fee,phonenum,languages)
                db.session.add(user)
                db.session.add(teahcer)
                db.session.commit()
            login_user(user, remember=True)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('private_route')
            return redirect(next_page)
        else:
            return Response("<p>invalid form</p>")
    else:
        return Response("<p>invalid form</p>")

    return render_template('login_signup.html', form=form)
                

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
