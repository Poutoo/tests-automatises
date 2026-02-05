import pytest
import sys
import os
import tempfile
from app.api import db as api_db # Import global db to check/reset if needed
import app.api

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def client():
    # Reset global db variable in app.api to ensure fresh init with new config
    app.api.db = None
    
    # Create a temporary file for the database
    db_fd, db_path = tempfile.mkstemp()
    
    # Create the app with the temporary database path
    flask_app = create_app({'TESTING': True, 'DATABASE': db_path})
    
    with flask_app.test_client() as client:
        yield client
    
    # Cleanup
    os.close(db_fd)
    os.unlink(db_path)
    # Reset global db again
    app.api.db = None

def test_calculator_endpoints(client):
    # Test Add
    response = client.get('/api/add/2/3')
    assert response.status_code == 200
    assert response.get_json() == {'result': 5.0}

    # Test Subtract
    response = client.get('/api/subtract/5/3')
    assert response.status_code == 200
    assert response.get_json() == {'result': 2.0}

    # Test Multiply
    response = client.get('/api/multiply/2/3')
    assert response.status_code == 200
    assert response.get_json() == {'result': 6.0}

    # Test Divide
    response = client.get('/api/divide/6/2')
    assert response.status_code == 200
    assert response.get_json() == {'result': 3.0}

def test_calculator_errors(client):
    # Test invalid input
    response = client.get('/api/add/a/3')
    assert response.status_code == 400
    assert 'error' in response.get_json()

    # Test division by zero
    response = client.get('/api/divide/1/0')
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_user_endpoints(client):
    # Test Add User
    user_data = {"username": "api_user", "email": "api@test.com"}
    response = client.post('/api/user', json=user_data)
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Utilisateur ajouté avec succès'}

    # Test Duplicate User
    response = client.post('/api/user', json=user_data)
    assert response.status_code == 409
    assert 'error' in response.get_json()

    # Test Get User
    response = client.get('/api/user/api_user')
    assert response.status_code == 200
    assert response.get_json()['username'] == "api_user"

    # Test Get Unknown User
    response = client.get('/api/user/unknown')
    assert response.status_code == 404

    # Test Delete User
    response = client.delete('/api/user/api_user')
    assert response.status_code == 200
    
    # Test Delete Unknown User
    response = client.delete('/api/user/unknown')
    assert response.status_code == 404
