"""Fixtures for passport model"""
import pytest
import uuid
import datetime
from src.models import Passport
from src.utilities.enums import SexEnum


@pytest.fixture(scope='module')
def new_passport(app, init_db, new_user):
    """Fixture to create a new passport"""
    new_user.save()
    passport = {
        "id": str(uuid.uuid4()),
        "user_id": new_user.id,
        "passport_type": 'P',
        "nationality": 'nigerian',
        "passport_no": 'B098712345',
        "date_of_birth": datetime.datetime(1990, 2, 14, 0, 0),
        "sex": SexEnum.male,
        "date_of_issue": datetime.datetime(2019, 2, 14, 0, 0),
        "date_of_expiry": datetime.datetime(2023, 2, 14, 0, 0)
    }
    return Passport(**passport)
