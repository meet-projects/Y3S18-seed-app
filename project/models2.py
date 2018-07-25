from project import db

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from flask import request, redirect, Flask, render_template
from flask_sqlalchemy import SQLAlchemy


class Journey(UserMixin, db.Model):

    __tablename__ = "journey"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = ### GET USER ID
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    duration = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    requirements = db.Column(db.String, nullable=False)
    people_range = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    picture = db.Column(db.String, nullable=False)



    def __init__(self, email):
        self.title = title
        self.description = description
        self.start_location = start_location
        self.end_location = end_location
        self.duration = duration
        self.category = category
        self.requirements = requirements
        self.people_range = people_range

    def __repr__(self):
        return 'Journey %d %s' % (self.id, self.email)

#db.drop_all()
db.create_all()