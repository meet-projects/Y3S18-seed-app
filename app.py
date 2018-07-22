# flask imports
from flask import Flask, render_template, request, redirect, url_for, Response, abort
from werkzeug.urls import url_parse
from auth import auth_module

# SQLAlchemy
from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager, logout_user, login_required, login_user

# setup
app = Flask(__name__)
app.secret_key = b'20ab823858d7f920a59014169703c7d91528edae3cd2ac2d' # change the secret
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app.register_blueprint(auth_module)

# constants
REMEMBER_ME = True

#================
# General Routes
#================

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')


#==============
# Login Routes
#==============

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         form = request.form
#         if form:
#             username = form['username']
#             password = form['password']
#             user = session.query(User).filter_by(username=username).first()
#             if user is None or not user.check_password(password):
#                 return abort(401)
#             login_user(user, remember=REMEMBER_ME)
#             next_page = request.args.get('next')
#             if not next_page or url_parse(next_page).netloc != '':
#                 next_page = url_for('private_route')
#             return redirect(next_page)
#     else:
#         return Response('''
#         <form action="" method="post">
#             <p><input type=text name=username>
#             <p><input type=password name=password>
#             <p><input type=submit value=Login>
#         </form>
#         ''')

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return Response('<p>Logged out</p>')

# @login_manager.user_loader
# def load_user(user_id):
#     return session.query(User).filter_by(id=user_id).first()