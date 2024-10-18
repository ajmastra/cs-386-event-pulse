from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# user schema for database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # every time an event is created, add id into this list
            # this will essentially store a list of all of the events owned by the user
    events = db.relationship('Event')

# event schema for database
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # foreign key means we need to pass a valid id of an existing user
            # 1 to n relationship from user -> event
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))