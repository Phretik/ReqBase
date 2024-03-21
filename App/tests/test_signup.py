import pytest
from flask import Flask, request
from ReqBase import auth, db, User, DB_NAME

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    with app.app_context():
        db.init_app(app)
        db.create_all()

    with app.test_request_context('/sign-up', method='GET'):
        yield app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

def test_sign_up_success(client, monkeypatch):
    # Mock form data and database interaction
    form_data = {
        'email': 'test@example.com',
        'firstname': 'Test',
        'password1': 'password123',
        'password2': 'password123'
    }
    def mock_db_query(email):
        return None
    monkeypatch.setattr(User.query, 'filter_by', mock_db_query)

    # Make POST request to sign-up endpoint
    response = client.post('/sign-up', data=form_data, follow_redirects=True)

    # Check if user was added to the database and redirected to requests page
    assert b'User account created.' in response.data
    assert b'Requests Page' in response.data
    assert User.query.filter_by(email=form_data['email']).first() is not None

def test_sign_up_existing_email(client, monkeypatch):
    # Mock form data and database interaction
    form_data = {
        'email': 'test@example.com',
        'firstname': 'Test',
        'password1': 'password123',
        'password2': 'password123'
    }
    def mock_db_query(email):
        return User(email='test@example.com', first_name='Test')
    monkeypatch.setattr(User.query, 'filter_by', mock_db_query)

    # Make POST request to sign-up endpoint
    response = client.post('/sign-up', data=form_data, follow_redirects=True)

    # Check if appropriate error message is displayed
    assert b'email already exists' in response.data
    assert b'Sign Up' in response.data  # Ensure sign-up page is rendered again

# Add more test cases as needed