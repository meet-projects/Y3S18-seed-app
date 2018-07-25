from project import db

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email          = db.Column(db.String, unique=True, nullable=False)
    password_hash  = db.Column(db.String, nullable=False)
    name           = db.Column(db.String, nullable=False)
    birthday       = db.Column(db.String, nullable=False)
    country        = db.Column(db.String, nullable=False)
    is_storyteller = db.Column(db.String, nullable=False)
    profession     = db.Column(db.String, nullable=False)
    city           = db.Column(db.String, nullable=False)
    number         = db.Column(db.String, nullable=False)
    bio            = db.Column(db.String, nullable=False)
    about          = db.Column(db.String, nullable=False)
    profile_img    = db.Column(db.String, nullable=False)
    reason         = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username       = username
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
        return 'User %d %s' % (self.id, self.username)

db.create_all()