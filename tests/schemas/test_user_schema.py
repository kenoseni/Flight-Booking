"""Module to test user schema"""

import pytest
from src.schemas import UserSchema
from tests.mocks.user import VALID_USER


class TestUserSchema:
    """Test User Schema"""

    def test_user_schema_deserialization_succeeds(self, new_user):
        """Test user schema serialization succeeds"""

        user_schema = UserSchema()
        user_data = dict(
            user_schema.load(VALID_USER).data)
        assert user_data['first_name'] == VALID_USER['first_name']
        assert user_data['last_name'] == VALID_USER['last_name']
        assert user_data['username'] == VALID_USER['username']
        assert user_data['email'] == VALID_USER['email']

    def test_user_schema_schema_serialization_succeeds(
            self, new_user, init_db):
        """Test user schema serialization succeeds

         Args:
            new_work_order (object): Fixture to create a new work_order
        """
        user = new_user.save()
        user_data = UserSchema().dump(user).data

        assert user.first_name == user_data['firstName']
        assert user.last_name == user_data['lastName']
        assert user.username == user_data['username']
        assert user.email == user_data['email']
