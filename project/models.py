from project import db

from flask import request, redirect, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email          = db.Column(db.String, unique=True, nullable=False)
    password_hash  = db.Column(db.String, nullable=False)
    name           = db.Column(db.String, nullable=False)
    # birthday       = db.Column(db.String, nullable=False)
    # country        = db.Column(db.String, nullable=False)
    # is_storyteller = db.Column(db.String, nullable=False)
    # profession     = db.Column(db.String, nullable=False)
    # city           = db.Column(db.String, nullable=False)
    # number         = db.Column(db.String, nullable=False)
    # bio            = db.Column(db.String, nullable=False)
    # about          = db.Column(db.String, nullable=False)
    # profile_img    = db.Column(db.String, nullable=False)
    # reason         = db.Column(db.String, nullable=False)

    def __init__(self, email,name,password):
        self.email       = email
        self.set_password(password)
        self.name           = name
        # self.birthday       = birthday
        # self.country        = country
        # self.is_storyteller = is_storyteller
        # self.profession     = profession
        # self.city           = city
        # self.number         = number
        # self.bio            = bio
        # self.about          = about

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User %d %s' % (self.id, self.email)

class Journey(UserMixin, db.Model):

    __tablename__ = "journey"

    id           = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id   = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title        = db.Column(db.String, nullable=False)
    description  = db.Column(db.String, nullable=False)
    location     = db.Column(db.String, nullable=False)
    duration     = db.Column(db.String, nullable=False)
    category     = db.Column(db.String, nullable=False)
    requirements = db.Column(db.String, nullable=False)
    people_range = db.Column(db.String, nullable=False)
    price        = db.Column(db.String, nullable=False)
    picture      = db.Column(db.String, nullable=False)


    def __init__(self):
       self.title = title
       self.description = description
       self.start_location = start_location
       self.end_location = end_location
       self.duration = duration
       self.category = category
       self.requirements = requirements
       self.people_range = people_range

    def __repr__(self):
        return 'Journey %d %s' % (self.id, self.title)

#db.drop_all()
db.create_all()

