from project import db

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=True)
    name1 = db.Column(db.String, nullable=True)
    name2 = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    phone1 = db.Column(db.String, nullable=True)
    phone2 = db.Column(db.String, nullable=True)

    def __init__(self, username, password, number, name, name1, name2, phone, phone1, phone2):
        self.username = username
        self.set_password(password)
        self.number = number
        self.name = name
        self.name1 = name1
        self.name2 = name2
        self.phone = phone
        self.phone1 = phone1
        self.phone2 = phone2

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User %d %s' % (self.id, self.username)