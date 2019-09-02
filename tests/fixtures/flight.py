"""Fixtures for flight model"""
import pytest
import uuid
import datetime
from src.models import Flight
from src.utilities.enums import FlightStatusEnum


@pytest.fixture(scope='module')
def new_flight(app, init_db, new_airplane):
    """Fixture to create a new flight"""
    new_airplane.save()
    flight = {
        "id": str(uuid.uuid4()),
        "airplane_id": new_airplane.id,
        "flight": 'FL111',
        "check_in": datetime.datetime(2019, 9, 10, 0, 0),
        "destination": 'Chicago',
        "departure": datetime.datetime(2019, 9, 10, 1, 0),
    }
    return Flight(**flight)
