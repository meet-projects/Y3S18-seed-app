from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

Base = declarative_base()

# class YourModel(Base):
#     __tablename__  = 'yourmodel'
#     id             = Column(Integer, primary_key=True)
    # ADD YOUR FIELD BELOW ID

# IF YOU NEED TO CREATE OTHER TABLE
# FOLLOW THE SAME STRUCTURE AS YourModel



class User(UserMixin, Base):
    '''
        Basic User model for authentication
    '''

    __tablename__ = 'user'
    id             = Column(Integer, primary_key=True)
    username       = Column(String(140))
    password_hash  = Column(String(140))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "%d/%s" % (self.id, self.name)