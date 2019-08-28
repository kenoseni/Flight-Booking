"""Fixtures for airplane model"""
import pytest
import uuid
from src.models import Airplane


@pytest.fixture(scope='module')
def new_airplane(app, init_db, new_user):
    """Fixture to create a new airplane"""
    airplane = {
       "id": str(uuid.uuid4()),
       "model": 'WTRYU897',
       "type": 'Boeing 747',
       "capacity": 230
    }
    return Airplane(**airplane)
