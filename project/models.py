from project import db

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User %d %s' % (self.id, self.email)


# TODO: Create your other models here
class YourModel(db.Model):
    
    __tablename__ = "yourmodel"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # fill in the rest of your fields and methods!

class Teacher(db.Model):

    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    name = db.Column(db.String) 
    city = db.Column(db.String)
    description = db.Column(db.String)
    cost = db.Column(db.Float)
    phone_num = db.Column(db.String)
    languages = db.Column(db.String)
    profile_picture = db.Column(db.String)
    car_type = db.Column(db.String)
    license_num = db.Column(db.String)

    '''def set_city(self, city):
        if  in list:
            self.city=city'''

    def __init__(self,
        user_id, 
        name,
        city,
        description,cost,phone_num,languages,profile_picture, car_type,license_num):
        self.user_id = user_id
        self.name=name
        self.city=city
        self.description=description
        self.cost=cost
        self.phone_num=phone_num
        self.languages=languages
        self.car_type=car_type
        self.license_num=license_num
        self.profile_picture=profile_picture

    def __repr__(self):
        return 'Teacher %d %s' % (self.id, self.name)

class Request(db.Model):

    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    phone_num = db.Column(db.String)
    date_d = db.Column('date_d', db.Integer)
    date_m = db.Column('date_m', db.Integer)
    date_y = db.Column('date_y', db.Integer)
    time = db.Column('time', db.Integer)
    teacher_id = db.Column(db.Integer, ForeignKey('teachers.id'))
    done = db.Column(db.Boolean)

    def __init__(self,name,phone_num,date_d,date_m,date_y,time,teacher_id,done):
        self.name = name
        self.phone_num = phone_num
        self.date = [date_d,date_m,date_y]
        self.time = time
        self.teacher_id = teacher_id
        self.done = done