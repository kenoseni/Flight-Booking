"""Module to test user model"""

import pytest
from src import db
from src.models import User


class TestUserModel:
    """Test user model"""
    def test_new_user_succeeds(self, init_db, new_user):
        """Test for creating a new user"""
        assert new_user == new_user.save()

    def test_user_model_string_representation_succeeds(self, new_user):
        """ Should compute the string representation of a user

        Args:
            new_user (object): Fixture to create a new user
        """
        assert repr(new_user) == f'<User: {new_user.username}>'
