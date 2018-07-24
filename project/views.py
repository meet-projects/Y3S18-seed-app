from flask import render_template
from flask_login import login_required

from . import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')
