from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# 'follow' table to handle friends
follow = db.Table(
    'follow',
    db.Column('following_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id'))
)

# user schema for database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # interests: either a list or a stirng
    interests = db.Column(db.String(150))
    
    
    # handles many to many relationship with itself for friends
    friends = db.relationship(
        'User',
        secondary = follow,
        primaryjoin = (follow.c.following_id == id),
        secondaryjoin = (follow.c.follower_id == id),
        backref = 'folllowing'
    )

    # every time an event is created, add id into this list
    # this will essentially store a list of all of the events owned by the user

    # establish the relationship of events to the user
    events = db.relationship('Event', backref='creator') 

    # Used to relate interests and users
    interests = db.relationship('Interest', secondary = 'user_interest', back_populates = 'users')

# event schema for database
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    date_of_event = db.Column(db.DateTime(timezone=True))
    time_of_event = db.Column(db.Time(timezone=True))
    location = db.Column(db.String(200))
    # foreign key means we need to pass a valid id of an existing user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Used to relate interests and events
    interests = db.relationship('Interest', secondary = 'event_interest', back_populates = 'events')

# interests schema
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


class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    # Used to relate interests and users
    users = db.relationship('User', secondary = 'user_interest', back_populates = 'interests')
    events = db.relationship('Event', secondary = 'event_interest', back_populates = 'interests')

# User to Interest many-to-many relation table
user_interest = db.Table(
    'user_interest',
    db.Column('user_id', db.ForeignKey('user.id')),
    db.Column('interest_id', db.ForeignKey('interest.id'))
)

# Event to Interest many-to-many relation table 
event_interest = db.Table(
    'event_interest',
    db.Column('event_id', db.ForeignKey('event.id')),
    db.Column('interest_id', db.ForeignKey('interest.id'))
    
)