from flask import Flask, render_template, request, redirect, url_for, Response, abort, Blueprint

from flask_login import LoginManager, logout_user, login_required, login_user

auth_module = Blueprint('auth_module', __name__)

login_manager = LoginManager()
login_manager.login_view = "login"

@auth_module.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        if form:
            username = form['username']
            password = form['password']
            user = session.query(User).filter_by(username=username).first()
            if user is None or not user.check_password(password):
                return abort(401)
            login_user(user, remember=REMEMBER_ME)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('private_route')
            return redirect(next_page)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')

@auth_module.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter_by(id=user_id).first()