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
    birthday       = db.Column(db.String, nullable=True)
    country        = db.Column(db.String, nullable=True)
    is_storyteller = db.Column(db.String, nullable=True)
    profession     = db.Column(db.String, nullable=True)
    city           = db.Column(db.String, nullable=True)
    number         = db.Column(db.String, nullable=True)
    bio            = db.Column(db.String, nullable=True)
    about          = db.Column(db.String, nullable=True)
    profile_img    = db.Column(db.String, nullable=True)
    reason         = db.Column(db.String, nullable=True)

    def __init__(self, email,name,password, birthday='', country='', is_storyteller='',profession='', city='', number='', bio='', about=''):
        self.email       = email
        self.set_password(password)
        self.name           = name
        self.birthday       = birthday
        self.country        = country
        self.is_storyteller = is_storyteller
        self.profession     = profession
        self.city           = city
        self.number         = number
        self.bio            = bio
        self.about          = about

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

    def __init__(self, creator_id='', title='', description='', location='', duration='', category='', requirements='', people_range='', picture='', price=''):
        self.creator_id    = creator_id
        self.title         = title
        self.description   = description
        self.location      = location
        self.duration      = duration
        self.category      = category
        self.requirements  = requirements
        self.people_range  = people_range
        self.picture       = picture
        self.price         = price


    def __repr__(self):
        return 'Journey %d %s' % (self.id, self.title)


# db.drop_all()
# db.create_all()

