import pytest
from flask import Flask
from flask_login import LoginManager
from website import create_app, db
from website.models import User

# create app for testing with pytest
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

# test for user signup with correct data
def test_signup(client):
    response = client.post('/sign-up', data={
        'email': 'test@example.com',
        'username': 'testuser',
        'firstName': 'Test',
        'password1': 'password123',
        'password2': 'password123'
    })
    # check for redirect
    assert response.status_code == 302  
    # follow the redirect
    response = client.get(response.headers['Location'])  
    assert b'Account created!' in response.data

# test login after creating an account
def test_login(client):
    client.post('/sign-up', data={
        'email': 'test@example.com',
        'username': 'testuser',
        'firstName': 'Test',
        'password1': 'password123',
        'password2': 'password123'
    })
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    })
    # check for redirect after login
    assert response.status_code == 302 
    # follow the redirect
    response = client.get(response.headers['Location'])  
    assert b'Logged in successfully!' in response.data

# test for creating an account with an email that already exists with an account
def test_duplicate_email(client):
    # create account
    client.post('/sign-up', data={
        'email': 'test@example.com',
        'username': 'testuser',
        'firstName': 'Test',
        'password1': 'password123',
        'password2': 'password123'
    })
    # try to create account with same email
    response = client.post('/sign-up', data={
        'email': 'test@example.com',
        'username': 'newuser',
        'firstName': 'New',
        'password1': 'password123',
        'password2': 'password123'
    })
    # email already has an account
    assert b'Email already has an account' in response.data

# test for too short of an email
def test_short_email(client):
    # try to add account with short email
    response = client.post('/sign-up', data={
        'email': 'abc',
        'username': 'testuser',
        'firstName': 'Test',
        'password1': 'password123',
        'password2': 'password123'
    })
    assert b'Email must be greater than 3 characters.' in response.data

# test logging in with email that doesnt exist
def test_incorrect_login(client):
    response = client.post('/login', data={
        'email': 'nonexistent@example.com',
        'password': 'password123'
    })
    assert b'Email does not exist.' in response.data

# test for trying to create an event without being logged in
def test_event_without_login(client):
    # create event, no user id
    response = client.post('/add-event', data={
        'event': 'Test Event',
        'description': 'This is a test event',
        'date_of_event': '2023-12-31',
        'time_of_event': '18:00',
        'type_of_event': 'Party',
        'location': 'Test Location'
    })
    # should redirect to login
    assert response.status_code == 302  

# test for signing up and not having matching passwords for the password confirmation
def test_non_matching_passwords(client):
    response = client.post('/sign-up', data={
        'email': 'test2@example.com',
        'username': 'testuser2',
        'firstName': 'Test',
        'password1': 'password123',
        'password2': 'password321'  # mismatched pass
    })
    assert b'Passwords do not match.' in response.data

# test for too short of a password
def test_short_password(client):
    response = client.post('/sign-up', data={
        'email': 'test3@example.com',
        'username': 'testuser3',
        'firstName': 'Test',
        'password1': 'short',  # too short
        'password2': 'short'
    })
    assert b'Password must be at least 7 characters.' in response.data

# test for signing in with the wrong password
def test_incorrect_password(client):
    client.post('/sign-up', data={
        'email': 'test4@example.com',
        'username': 'testuser4',
        'firstName': 'Test',
        'password1': 'password123',
        'password2': 'password123'
    })
    response = client.post('/login', data={
        'email': 'test4@example.com',
        'password': 'wrongpassword'  # incorrect password
    })
    assert b'Incorrect password, try again.' in response.data
