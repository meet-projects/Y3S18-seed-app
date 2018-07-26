from project import db

from sqlalchemy import and_, or_
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username            = db.Column(db.String, unique=True, nullable=False)
    displayname            = db.Column(db.String)
    password_hash       = db.Column(db.String, nullable=False)

    def __init__(self, username, displayname, password):
        self.username = username
        self.displayname = displayname
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User %d %s' % (self.id, self.username)

class Post(db.Model):
    __tablename__='posts'
    id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AuthorID       = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ArtURL         = db.Column(db.String)
    Title          = db.Column(db.String(20), nullable=False)
    Text           = db.Column(db.String, nullable=False)
    Rating         = db.Column(db.Integer)

    def __init__(self, AuthorID, Title, Text):
        self.AuthorID = AuthorID
        self.ArtURL = ""
        self.Title = Title
        self.Text = Text
        self.Rating = 0

    def relate(self, userid):
        getpostlike = Like.query.filter(and_((postID == self.id), (userID == userid))).first()
        if getpostlike is None:
            add_like = Like(userid. self.id)
            db.session.add(add_like)
        else:
            db.session.delete(getpostlike)

        self.get_rating()
        db.session.commit()

    def get_rating(self):
        getlikes = Like.query.filter(postID == self.id).all()
        self.Rating = len(getlikes)

    def __repr__(self):
        return "post " + str(self.id) + " " + str(self.Title) + " " + str(self.Text)

    # def set_rating(self,new_rating):
    #     self.Rating = new_rating

    # def get_rating():
    #     return self.Rating

class Like(db.Model):
    __tablename__='likes'
    id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID         = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    postID         = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    def __init__(self, userID, postID):
        self.userID = userID
        self.postID = postID