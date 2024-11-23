from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.event import listens_for

# List of default interests to be added
DEFAULT_INTERESTS = ("Live Music", "Theatre", "Political Event", "Community Events")

# 'follow' table to handle friends
follow = db.Table(
    'follow',
    db.Column('following_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('status', db.String(10), default='pending')  # 'pending' or 'accepted'
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
    # Admin user 
    is_admin = db.Column(db.Boolean, default=False)
    # Events they are 'interested in'
    events_interested_in = db.relationship(
        'Event',
        secondary = 'users_interested_in_events',
        back_populates = 'users_interested'
    )
    
    # handles many to many relationship with itself for friends
    friends = db.relationship(
        'User',
        secondary = follow,
        primaryjoin = (follow.c.following_id == id),
        secondaryjoin = (follow.c.follower_id == id),
        backref = 'folllowing'
    )

    # initialize send friend request button
        # sends friend request to another user
    def send_friend_request(self, to_user):

        # check if the target user has already sent a request to the current user
        existing_request = db.session.query(follow).filter_by(
            following_id=to_user.id, follower_id=self.id, status='pending'
        ).first()

        # if there WAS an existing friend request send to the current user
        if existing_request:
            # auto accept on both users behalfs
            db.session.execute(
                follow.update()
                .where(follow.c.following_id == to_user.id, follow.c.follower_id == self.id)
                .values(status='accepted')
            )
            db.session.execute(
                follow.update()
                .where(follow.c.following_id == self.id, follow.c.follower_id == to_user.id)
                .values(status='accepted')
            )

            # commit changes to db
            db.session.commit()

            # flash success
            flash(f"You are now friends with {to_user.username}!", category='success')

        # otherwise, create a new pending friend request
        else:

            # create new request row on table
            db.session.execute(
                follow.insert().values(following_id=self.id, follower_id=to_user.id, status='pending')
            )

            # commit to db
            db.session.commit()

            # flash success
            flash(f"Friend request sent to {to_user.username}.", category='success')

    # initialize accept friend request button
        # accepts a friend request from another user
    def accept_friend_request(self, from_user):

        # update the follow column, and set the users to friends with each other's ids with status accepted
        db.session.execute(
            follow.update()
            .where(follow.c.following_id == from_user.id, follow.c.follower_id == self.id)
            .values(status='accepted')
        )
        # commit to the database
        db.session.commit()

    # initalize get friends function
        # retrieves all users who have an accepted friend status with the current_user
    def get_friends(self):

        # return a list of users who are friends with current user
        return [u for u in self.friends if follow.query.filter_by(
            following_id=self.id, follower_id=u.id, status='accepted'
        ).first()]

    # initialize get pending requests functions
        # retrieve all pending friend requests to the current_user
    def get_pending_requests(self):

        # return the list of users who have send a pending friend request to current_user
        return [u for u in self.friends if follow.query.filter_by(
            following_id=u.id, follower_id=self.id, status='pending'
        ).first()]

    # every time an event is created, add id into this list
    # this will essentially store a list of all of the events owned by the user
    # establish the relationship of events to the user
    events = db.relationship('Event', backref='creator', cascade='all, delete')

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

    # Events they are 'interested in'
    users_interested = db.relationship(
        'User',
        secondary = 'users_interested_in_events',
        back_populates = 'events_interested_in'
    )

# User to event many-to-many relation for event saving aka 'interested in'
users_interested_in_events = db.Table(
    'users_interested_in_events',
    db.Column('event_id', db.ForeignKey('event.id')),
    db.Column('user_id', db.ForeignKey('user.id'))
)

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
    likes = db.relationship('Like', back_populates='comment', cascade='all, delete')

# interests schema
class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    # Used to relate interests and users
    users = db.relationship('User', secondary = 'user_interest', back_populates = 'interests')
    events = db.relationship('Event', secondary = 'event_interest', back_populates = 'interests')

# listener to add default interests from list when table is created
@listens_for(Interest.__table__, 'after_create')
def insert_default_interests(target, connection, **kwargs):
    """Insert default interests into the database after the table is created."""
    for interest_name in DEFAULT_INTERESTS:
        connection.execute(target.insert().values(name=interest_name))

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