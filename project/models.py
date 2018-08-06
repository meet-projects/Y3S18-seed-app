from project import db
from datetime import datetime

from sqlalchemy import and_, or_
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
	__tablename__ = "users"
	id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username            = db.Column(db.String, unique=True, nullable=False)
	displayname         = db.Column(db.String)
	#email               = db.Column(db.String, unique=True, nullable=False)
	bio                 = db.Column(db.String, default = "Hi, i'm using Artflict!")
	profile_pic_url     = db.Column(db.String, nullable=True)
	password_hash       = db.Column(db.String, nullable=False)

	def __init__(self, username, displayname, password):
		self.username = username
		self.displayname = displayname
		self.set_password(password)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def get_followers(self):
		get_followers = Follower.query.filte_by(followedID = self.id)
		return get_followers

	def get_followed(self):
		get_followed = Follower.query.filte_by(followerID = self.id)
		return get_followed

	def __repr__(self):
		return 'User %d %s' % (self.id, self.username)

class Post(db.Model):
	__tablename__='posts'
	id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
	AuthorID       = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	ArtURL         = db.Column(db.String)
	ArtistID       = db.Column(db.Integer, db.ForeignKey('users.id'))
	ArtistNotes    = db.Column(db.String)
	Title          = db.Column(db.String(20), nullable=False)
	Text           = db.Column(db.String, nullable=False)
	Rating         = db.Column(db.Integer)
	Date           = db.Column(db.String, nullable=False)

	def __init__(self, AuthorID, Title, Text):
		self.AuthorID = AuthorID
		self.Title = Title
		self.Text = Text
		self.Date = self.format_date()
		self.Rating = 0

	def relate(self):
		userid = current_user.id
		getpostlike = Like.query.filter_by(postID = self.id).filter_by(UserID = userid).first()
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

	def format_rating(self):
		rating = float(self.Rating)
		if rating < 1000:
			return str(rating)
		elif rating < 1000000:
			new_rating = round(rating / 1000, 1)
			return  new_rating + "K"
		elif rating < 1000000000:
			new_rating = round(rating / 1000000, 1)
			return new_rating + "M"
		else:
			return "LOTS"

	def format_date(self):
		now = datetime.now()
		return str(now.month) + " - " + str(now.day) + " - " + str(now.year)

	def get_description1(self):
		return self.Text[:10] 


	def get_description2(self):
		return self.Text[10:300] + "."


	def get_title(self):
		return self.Title[:100] + "."






	def __repr__(self):
		return "post " + str(self.id) + " " + str(self.Title) + " " + str(self.Text)

class Like(db.Model):
	__tablename__='likes'
	id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
	userID         = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	postID         = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

	def __init__(self, userID, postID):
		self.userID = userID
		self.postID = postID

class Follower(db.Model):
	__tablename__ = 'followers'
	id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
	followerID     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	followedID     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __init__(self, followerID, followedID):
		 self.followerID = followerID
		 self.followedID = followedID
