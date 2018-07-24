from flask import render_template
from flask_login import login_required

from . import app


@app.route('/')
def feed():
    return render_template('feed.html')



@app.route('/form')
@login_required
def private_route():
    return render_template('form.html')
