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
    events = db.relationship('Event', backref='creator', cascade='all, delete')

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
    comments = db.relationship('Comment', back_populates='event', cascade='all, delete')

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
    event = db.relationship('Event', back_populates='comments')
    likes = db.relationship('Like', back_populates='comment', cascade='all, delete')

# like schedma for database
class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # pass existing user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # pass existing comment id
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)
    # relationships
    user = db.relationship('User', backref='likes')
    comment = db.relationship('Comment', back_populates='likes')