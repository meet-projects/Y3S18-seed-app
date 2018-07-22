from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# REPLACE YourModel with the one that you created in model.py
from model import Base, User, YourModel

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)