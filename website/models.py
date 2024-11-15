from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# user schema for database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # interests: either a list or a stirng
    interests = db.Column(db.String(150))
    
    # every time an event is created, add id into this list
    # this will essentially store a list of all of the events owned by the user

    # establish the relationship of events to the user
    events = db.relationship('Event', backref='creator') 

# event schema for database
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    date_of_event = db.Column(db.DateTime(timezone=True))
    time_of_event = db.Column(db.Time(timezone=True))
    type_of_event = db.Column(db.String(200))
    location = db.Column(db.String(200))
    # foreign key means we need to pass a valid id of an existing user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# interests
# class Interests(db.Model): yeah idk lol -zach


# comment schema for database
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    # forieng key so we have to pass existing user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # we have to pass existing event
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    #relationships
    user = db.relationship('User', backref='comments')
    event = db.relationship('Event', backref='comments')