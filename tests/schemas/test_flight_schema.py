"""Module to test flight schema"""

import pytest
import datetime
from src.schemas import FlightSchema
from tests.mocks.flight import VALID_FLIGHT_DETAILS


class TestFlightSchema:
    """Test Flight Schema"""

    def test_flight_schema_deserialization_succeeds(self):
        """Test flight schema deserialization succeeds"""

        flight_schema = FlightSchema()
        flight_data = dict(
            flight_schema.load(VALID_FLIGHT_DETAILS).data)
        assert flight_data['flight'] == VALID_FLIGHT_DETAILS[
            'flight']
        assert flight_data['destination'] == VALID_FLIGHT_DETAILS[
            'destination']
        assert flight_data['airplane_id'] == VALID_FLIGHT_DETAILS[
            'airplaneId']
        assert flight_data['departure'] == datetime.datetime.strptime(
            VALID_FLIGHT_DETAILS['departure'], '%Y-%m-%d %H:%M:%S')
        assert flight_data['check_in'] == datetime.datetime.strptime(
            VALID_FLIGHT_DETAILS['checkIn'], '%Y-%m-%d %H:%M:%S')
        assert flight_data['status'].value == VALID_FLIGHT_DETAILS['status']

    def test_flight_schema_serialization_succeeds(
            self, new_flight, init_db):
        """Test flight schema serialization succeeds

         Args:
            new_flight (object): Fixture to create a new flight
        """
        flight = new_flight.save()
        flight_data = FlightSchema().dump(flight).data

        assert flight.destination == flight_data['destination']
        assert flight.status.value == flight_data['status']
        assert flight.flight == flight_data['flight']
        assert flight.departure == datetime.datetime.strptime(
            flight_data['departure'], '%Y-%m-%dT%H:%M:%S+00:00')
        assert flight.check_in == datetime.datetime.strptime(
            flight_data['checkIn'], '%Y-%m-%dT%H:%M:%S+00:00')
        assert isinstance(flight_data['airplane'], dict)
