"""Module to test airplane schema"""

import pytest
from src.schemas import AirplaneSchema
from tests.mocks.airplane import VALID_AIRPLANE_DETAILS


class TestAirplaneSchema:
    """Test Airplane Schema"""

    def test_airplane_schema_deserialization_succeeds(self):
        """Test aiplane schema deserialization succeeds"""

        airplane_schema = AirplaneSchema()
        airplane_data = dict(
            airplane_schema.load(VALID_AIRPLANE_DETAILS).data)
        assert airplane_data['model'] == VALID_AIRPLANE_DETAILS['model']
        assert airplane_data['type'] == VALID_AIRPLANE_DETAILS[
            'type']
        assert airplane_data['capacity'] == VALID_AIRPLANE_DETAILS[
            'capacity']

    def test_airplane_schema_schema_serialization_succeeds(
            self, new_airplane, init_db):
        """Test airplane schema serialization succeeds

         Args:
            new_airplane (object): Fixture to create a new airplane
        """
        airplane = new_airplane.save()
        airplane_data = AirplaneSchema().dump(airplane).data

        assert airplane.model == airplane_data['model']
        assert airplane.type == airplane_data['type']
        assert airplane.capacity == airplane_data['capacity']
