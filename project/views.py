from flask import render_template
from flask_login import login_required

from . import app

import os
from twilio.rest import Client

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')
