import pytest

from app import create_app
from unittest.mock import Mock, patch

@pytest.fixture
def app():
    # TODO: be able to seperate test config from other env
    app = create_app('test')
    
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# TODO: set up connections to test database for testing purpose
# It may be too complex later on to mock the database response
# Espacially when the methods are usually chained. 
# @pytest.fixture()
# def mock_db():
#     mock_db = Mock()
#     patch.object(db, 'database_proxy', mock_db)
#     return mock_db

@pytest.fixture()
def user():
    user_data = {
        "id": "test_user",
        "account_status": "active",
        "country_code": "ff",
        "email": "test_email@example.com",
        "first_name": "Bob",
        "last_name": "Moyer Second",
        "password_hash": "TrEtnhWdeNykWngFBUObCbmUGyDFhiPVFhELzTptIfTsNRSqudxMnOfOCzaxUeZA",
        "password_salt": "hUsqDnfwtRhbOyRWxsTXuxmzxVEwjjeGFUgcohQUZQFSBYeXToZrszhIZmTqGTJM"
    }
    return user_data