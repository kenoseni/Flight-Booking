"""Module to test flight model"""

import pytest
from src import db
from src.models import Flight


class TestFlightModel:
    """Test flight model"""
    def test_new_flight_succeeds(self, init_db, new_flight):
        """Test for creating a new flight"""
        assert new_flight == new_flight.save()

    def test_flight_model_string_representation_succeeds(self, new_flight):
        """ Should compute the string representation of a flight

        Args:
            new_flight (object): Fixture to create a new flight
        """
        assert repr(new_flight) == f'<Flight: {new_flight.flight}>'
