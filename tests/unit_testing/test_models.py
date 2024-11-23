import pytest
from datetime import datetime, time
from website import create_app, db
from website.models import User, Event, Comment, Interest, Like

@pytest.fixture
def test_client():
    """Set up a Flask test client and database for testing."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()

# test user creation
def test_user_creation(test_client):
    """Test user creation."""
    user = User(email="testuser@example.com", username="testuser", password="password123")
    db.session.add(user)
    db.session.commit()

    assert user in db.session
    assert user.email == "testuser@example.com"
    assert user.username == "testuser"

def test_event_creation(test_client):
    """Test event creation and its relationship to a user."""
    user = User(email="organizer@example.com", username="organizer", password="password123")
    db.session.add(user)
    db.session.commit()

    event = Event(
        title="Test Event",
        description="A fun event!",
        date_of_event=datetime(2024, 11, 22),
        time_of_event=time(18, 0),
        location="Test Location",
        user_id=user.id
    )
    db.session.add(event)
    db.session.commit()

    assert event in db.session
    assert event.title == "Test Event"
    assert event.creator == user

def test_comment_creation(test_client):
    """Test comment creation and its relationship to a user and event."""
    user = User(email="commenter@example.com", username="commenter", password="password123")
    event = Event(
        title="Comment Event",
        description="An event with comments",
        date_of_event=datetime(2024, 11, 22),
        time_of_event=time(19, 0),
        location="Another Location",
        user_id=user.id
    )
    db.session.add_all([user, event])
    db.session.commit()

    comment = Comment(content="Great event!", user_id=user.id, event_id=event.id)
    db.session.add(comment)
    db.session.commit()

    assert comment in db.session
    assert comment.content == "Great event!"
    assert comment.user == user
    assert comment.event == event

def test_interest_creation(test_client):
    """Test interest creation and its relationship to users and events."""
    interest = Interest(name="Tech")
    db.session.add(interest)
    db.session.commit()

    assert interest in db.session
    assert interest.name == "Tech"

    # Add a user and event to the interest
    user = User(email="interested@example.com", username="interested_user", password="password123")
    event = Event(
        title="Tech Event",
        description="A tech-related event",
        date_of_event=datetime(2024, 12, 1),
        time_of_event=time(14, 0),
        location="Tech Location",
        user_id=user.id
    )
    db.session.add_all([user, event])
    db.session.commit()

    interest.users.append(user)
    interest.events.append(event)
    db.session.commit()

    assert user in interest.users
    assert event in interest.events

def test_like_creation(test_client):
    """Test like creation and its relationship to a user and comment."""
    user = User(email="liker@example.com", username="liker", password="password123")
    db.session.add(user)
    db.session.commit() 

    event = Event(
        title="Like Event",
        description="An event to like",
        date_of_event=datetime(2024, 12, 10),
        time_of_event=time(16, 0),
        location="Like Location",
        user_id=user.id
    )
    db.session.add(event)
    db.session.commit() 

    comment = Comment(content="I like this event!", user_id=user.id, event_id=event.id)
    db.session.add(comment)
    db.session.commit()
    like = Like(user_id=user.id, comment_id=comment.id)
    db.session.add(like)
    db.session.commit()

    assert like in db.session
    assert like.user == user
    assert like.comment == comment

