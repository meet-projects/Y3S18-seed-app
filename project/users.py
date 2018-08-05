from flask import (
        Blueprint, redirect, render_template,
        Response, request, url_for
)
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError

from project import db
from project.forms import RegisterForm, LoginForm
from project.models import User



from flask import request, redirect, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from project.models import Journey, User, Ratings, Notification, Wishlist, Question




users_bp = Blueprint('users', __name__)

# current_user = 'Not Logged In'

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data
            is_storyteller = False
            user = User.query.filter_by(email=email).first()
            if user != None:
                return Response ("<p> account already exists <p>")
                return render_template('register.html', form=form)
            else:
                user = User(email=email, name= name, password= password, is_storyteller= is_storyteller)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('users.login'))

    else:
        logout_user()
        return render_template('register.html', form=form)
   

                

@users_bp.route('/', methods=['GET', 'POST'])
def browse():
    all_journeys = Journey.query.all()
    return render_template('browse.html', all_journeys=all_journeys)

@users_bp.route('/login', methods=['GET','POST'])
def login():
    print(request.form)
    form = LoginForm(request.form)
    if request.method == 'POST':
        print(form.email.data)
        print(form.password.data)
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user is None or not user.check_password(password):
                return Response("<p>Incorrect email or password</p>")
            login_user(user, remember=True)

           
#             next_page = request.args.get('next')
#             if not next_page or url_parse(next_page).netloc != '':
#                 #return render_template('browse.html', current_user=user)
#                 next_page = url_for('browse')
            # next_page = request.args.get('next')
            # if not next_page or url_parse(next_page).netloc != '':
            #     next_page = url_for('private_route')

            return redirect(url_for('users.browse'))
        else:
            return Response("<p>invalid form</p>")
    else:
        return render_template('login.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()

    form = LoginForm(request.form)
    return render_template('login.html', form=form)

# def login():
 #   print(request.form)
  #  form = LoginForm(request.form)
   # if request.method == 'POST':
    #    print(form.email.data)
     #   print(form.password.data)
      #  if form.validate_on_submit():
       #     email = form.email.data
        #    password = form.password.data
         #   user = User.query.filter_by(email=email).first()
          #  if user is None or not user.check_password(password):
           #     return Response("<p>Incorrect email or password</p>")
            #login_user(user, remember=True)