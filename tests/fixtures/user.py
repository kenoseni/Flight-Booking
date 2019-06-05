"""Fixtures for user model"""
import pytest
from src.models import User
from tests.mocks.user import VALID_USER

@pytest.fixture(scope='module')
def new_user(app):
    """Fixture to create a new user"""
    return User(**VALID_USER)
