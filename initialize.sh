#!/bin/bash

if [[ -e y3-venv ]]; then
    source y3-venv/bin/activate
else
    sudo pip install virtualenv
    virtualenv -p $(which python3) y3-venv
    source y3-venv/bin/activate
    pip install -r requirements.txt
fi

export FLASK_APP='project'
export FLASK_ENV='development'
export FLASK_DEBUG=1
