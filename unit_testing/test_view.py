import pytest
from website import create_app, db
from website.models import User, Event

# create an app for unit testing
@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_view(client):
    response = client.get('/')
    assert response.status_code == 302  # Redirect to login if not logged in

# test for adding an event
def test_add_event(client):
    # create test user
    client.post('/sign-up', data={
        'email': 'test@example.com',
        'username': 'testuser',
        'firstName': 'Test',
        'password1': 'password123',
        'password2': 'password123'
    })
    # login with the test user
    client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    })
    # create an event for the test user
    response = client.post('/add-event', data={
        'event': 'Test Event',
        'description': 'This is a test event',
        'date_of_event': '2023-12-31',
        'time_of_event': '18:00',
        'type_of_event': 'Party',
        'location': 'Test Location'
    })
    # check for redirect
    assert response.status_code == 302  
    # follow the redirect
    response = client.get(response.headers['Location'])  
    assert b'Event added successfully!' in response.data
