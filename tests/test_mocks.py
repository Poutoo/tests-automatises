import pytest
import sys
import os
from unittest.mock import MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
import app.api

@pytest.fixture
def client(mocker):
    app.api.db = None

    mock_db_class = mocker.patch('app.api.Database')
    mock_db_instance = mock_db_class.return_value
    
    mock_db_instance.connect.return_value = None
    
    flask_app = create_app({'TESTING': True, 'DATABASE': ':memory:'})
    
    with flask_app.test_client() as client:
        client.mock_db = mock_db_instance
        yield client
    
    app.api.db = None

def test_add_user_mock(client):
    client.mock_db.add_user.return_value = True
    
    user_data = {"username": "mock_user", "email": "mock@test.com"}
    response = client.post('/api/user', json=user_data)
    
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Utilisateur ajouté avec succès'}
    client.mock_db.add_user.assert_called_with("mock_user", "mock@test.com")
    
    client.mock_db.add_user.return_value = False
    
    response = client.post('/api/user', json=user_data)
    
    assert response.status_code == 409
    assert 'error' in response.get_json()

def test_database_connection_error(client):
    client.mock_db.connect.side_effect = Exception("Connection failed")
    
    try:
        response = client.get('/api/test')
        assert response.status_code == 500
    except Exception as e:
        print(f"Caught expected exception: {e}")
        assert "Connection failed" in str(e)
    
    client.mock_db.connect.side_effect = None

