#!/bin/bash

old_pwd=$(pwd)
cd ~/

if [[ -e y2-venv ]]; then
    source ~/y2-venv/bin/activate
else
     sudo apt-get install virtualenv
     virtualenv -p $(which python3) y2-venv
     source ~/y2-venv/bin/activate
     pip install -r $old_pwd/requirements.txt
fi
cd $old_pwd

export FLASK_APP=app.py
export FLASK_DEBUG=1