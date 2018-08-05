from project import db

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    booster_seat_id = db.Column(db.String, unique=True, nullable=False)
    name1 = db.Column(db.String, nullable=True)
    name2 = db.Column(db.String, nullable=True)
    name3 = db.Column(db.String, nullable=True)
    phone1 = db.Column(db.String, nullable=True)
    phone2 = db.Column(db.String, nullable=True)
    phone3 = db.Column(db.String, nullable=True)
    relation1 = db.Column(db.String, nullable=True)
    relation2 = db.Column(db.String, nullable=True)
    relation3 = db.Column(db.String, nullable=True)
    flag = db.Column(db.Integer, nullable=False)

    def __init__(self, username, password, number, booster_seat_id):
        self.username = username
        self.set_password(password)
        self.number = number
        self.flag = 0
        self.booster_seat_id = booster_seat_id


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User %d %s' % (self.id, self.username)

'''class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String, nullable=False)
    relation = db.Column(db.String(50), nullable=False)
    user = db.relationship('User', backref='user', lazy=True)'''
