from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

Base = declarative_base()

class User(UserMixin, Base):
    '''
        Basic User model for authentication
    '''

    __tablename__ = 'user'
    UserID         = Column(Integer, primary_key=True, autoincrement=True)
    username       = Column(String(40), unique=True, nullable= False)
    password_hash  = Column(String(40), nullable = False)
    email          = Column(String, unique = True, nullable=False)
    bio            = Column(String, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "%d/%s" % (self.id, self.name)

class Post(Base):
    __tablename__='posts'
    PostID         = Column(Integer, primary_key=True, autoincrement=True)
    AuthorID       = Column(Integer, ForeignKey())
    Title          = Column(String(20), nullable=False)
    Text           = Column(String, nullable=False)
    Rating         = Column(Integer)
