"""Module to test passport model"""

import pytest
from src import db
from src.models import Passport


class TestPassportModel:
    """Test passport model"""
    def test_new_passport_succeeds(self, init_db, new_passport):
        """Test for creating a new passport"""
        assert new_passport == new_passport.save()

    def test_passport_model_string_representation_succeeds(self, new_passport):
        """ Should compute the string representation of a passport

        Args:
            new_passport (object): Fixture to create a new passport
        """
        assert repr(new_passport) == f'<Passport: {new_passport.user_id}>'
