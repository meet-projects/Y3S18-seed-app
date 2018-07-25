from flask import render_template
from flask_login import login_required
from project import db
from . import app
from project.models import User



@app.route('/')
def feed():
	teacher=db.session.query()
    return render_template('form.html')



@app.route('/form')
@login_required
def private_route():
    return render_template('form.html')
