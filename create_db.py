import os
from project import db
from project.models import *

dbfile = 'project/project.db'
if os.path.exists(dbfile):
    os.remove(dbfile)

db.create_all()
