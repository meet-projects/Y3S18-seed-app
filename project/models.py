from project import db

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
    __tablename__ = "users"
    userID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User %d %s' % (self.userID, self.username)

class Post(db.Model):
    __tablename__='posts'
    postID         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    authorID       = db.Column(db.Integer, db.ForeignKey('users.userID'))
    title          = db.Column(db.String(20), nullable=False)
    text           = db.Column(db.String, nullable=False)
    rating         = db.Column(db.Integer, default = 0)

    def __init__(self, authorID, title, text, rating):
        self.authorID = authorID
        self.title = title
        self.text = text
        self.rating = rating

