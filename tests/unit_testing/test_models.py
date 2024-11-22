import pytest
from website import create_app, db, DB_NAME
from website.models import User, Event
from sqlalchemy.exc import IntegrityError

# create the app for unit testing
@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

# testing for user model
def test_user_model(app):
    with app.app_context():
        user = User(email='test@example.com', username='testuser', password='hashed_password', first_name='Test')
        db.session.add(user)
        db.session.commit()
        assert user.id is not None

# testing for event model
def test_event_model(app):
    with app.app_context():
        user = User(email='test@example.com', username='testuser', password='hashed_password', first_name='Test')
        db.session.add(user)
        db.session.commit()
        
        event = Event(title='Test Event', description='This is a test event', user_id=user.id)
        db.session.add(event)
        db.session.commit()
        assert event.id is not None

# test to evaluate the required fields when creating an event
def test_event_required_fields(app):
    with app.app_context():
        user = User(email='test@example.com', username='testuser', password='hashed_password', first_name='Test')
        db.session.add(user)
        db.session.commit()

        event = Event(description='This event has no title', user_id=user.id)  # Missing title
        db.session.add(event)
        # expecting an IntegrityError
        with pytest.raises(IntegrityError):  
            db.session.commit()