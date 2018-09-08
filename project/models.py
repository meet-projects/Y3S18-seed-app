from project import db

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import geonamescache

gc = geonamescache.GeonamesCache()


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    account_type = db.Column(db.String,  nullable=False)

    def __init__(self, email, password,account_type):
        self.email = email
        self.set_password(password)
        self.account_type=account_type

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
    fname = db.Column(db.String) 
    lname = db.Column(db.String) 
    city = db.Column(db.String)
    description = db.Column(db.String)
    cost = db.Column(db.Float)
    phone_num = db.Column(db.String)
    languages = db.Column(db.String)
    profile_picture = db.Column(db.String)
    gearbox= db.Column(db.String)

    '''def set_city(self, city):
        if  in list:
            self.city=city'''

    def __init__(self,
        user_id, 
        fname,lname,
        city,
        description,
        cost,
        phone_num,
        languages,
        profile_picture,
        gearbox):
        self.user_id = user_id
        self.fname=fname
        self.lname=lname
        self.city=city
        self.description=description
        self.cost=cost
        self.phone_num=phone_num
        self.languages=languages
        self.profile_picture=profile_picture
        self.gearbox=gearbox

    def __repr__(self):
        return 'Teacher %d %s %s' % (self.id, self.fname, self.lname)

class Request(db.Model):

    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id= db.Column(db.Integer,ForeignKey('students.id'))
    student_fname = db.Column(db.String)
    teacher_id = db.Column(db.Integer, ForeignKey('teachers.id'))
    done = db.Column(db.Boolean)

    def __init__(self,student_id,student_fname,teacher_id,done):
        self.student_id=student_id
        self.student_fname=student_fname
        self.teacher_id = teacher_id
        self.done = done


class Student(db.Model):

    __tablename__="students"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id=db.Column(db.Integer, ForeignKey('users.id'))
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    phone_num = db.Column(db.String)
    gearbox=db.Column(db.String)
    city=db.Column(db.String)
    min_price =db.Column(db.Integer)
    max_price=db.Column(db.Integer)
    languages=db.Column(db.String)


    def __init__(self, user_id,fname,lname,phone_num,gearbox,city,min_price,max_price,languages):
        self.user_id=user_id
        self.fname=fname
        self.lname=lname
        
        self.phone_num=phone_num
        self.gearbox=gearbox
        self.city=city
        self.min_price=min_price
        self.max_price=max_price
        self.languages=languages
        self.profile_picture="https://static.thenounproject.com/png/214280-200.png"
        

class City(db.Model):

    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String)
    country = db.Column(db.String)

    def __repr__(self):
        return 'City %d %s' % (self.id, self.city)
