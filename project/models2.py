from project import db

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class Journey(UserMixin, db.Model):

    __tablename__ = "journey"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    start_location = db.Column(db.String, nullable=False)
    end_location = db.Column(db.String, nullable=False)
    duration = db.Column(db.String, nullable=False)
    people_type = db.Column(db.String, nullable=False)
    requirements = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.title = title
        self.description = description
        self.start_location = start_location
        self.end_location = end_location
        self.duration = duration
        self.people_type = people_type
        self.requirements = requirements

    def __repr__(self):
        return 'Journey %d %s' % (self.id, self.username)