"""Module to test airplane model"""

import pytest
from src import db
from src.models import Airplane


class TestAirplaneModel:
    """Test airplane model"""
    def test_new_airplane_succeeds(self, init_db, new_airplane):
        """Test for creating a new airplane"""
        assert new_airplane == new_airplane.save()

    def test_airplane_model_string_representation_succeeds(self, new_airplane):
        """ Should compute the string representation of a airplane

        Args:
            new_airplane (object): Fixture to create a new airplane
        """
        assert repr(new_airplane) == f'<Airplane: {new_airplane.type}>'
