import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import Database

@pytest.fixture
def database():
    db = Database(':memory:')
    db.connect()
    yield db
    db.disconnect()

def test_add_user(database):
    assert database.add_user("test_user", "user@example.com") == True
    # Test duplication
    assert database.add_user("test_user", "other@example.com") == False

def test_get_user(database):
    database.add_user("test_user", "user@example.com")
    user = database.get_user("test_user")
    assert user is not None
    assert user['username'] == "test_user"
    assert user['email'] == "user@example.com"
    
    assert database.get_user("non_existent") is None

def test_delete_user(database):
    database.add_user("test_user", "user@example.com")
    assert database.delete_user("test_user") == True
    assert database.delete_user("test_user") == False