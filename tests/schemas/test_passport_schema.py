"""Module to test passport schema"""

import pytest
import datetime
from src.schemas import PassportSchema
from tests.mocks.passport import VALID_PASSPORT_DETAILS


class TestPassportSchema:
    """Test Passport Schema"""

    def test_passport_schema_deserialization_succeeds(self):
        """Test user schema deserialization succeeds"""

        passport_schema = PassportSchema()
        passport_data = dict(
            passport_schema.load(VALID_PASSPORT_DETAILS).data)
        assert passport_data['user_id'] == VALID_PASSPORT_DETAILS['userId']
        assert passport_data['passport_type'] == VALID_PASSPORT_DETAILS[
            'passportType']
        assert passport_data['nationality'] == VALID_PASSPORT_DETAILS[
            'nationality']
        assert passport_data['passport_no'] == VALID_PASSPORT_DETAILS[
            'passportNumber']
        assert passport_data['date_of_birth'] == datetime.datetime.strptime(
            VALID_PASSPORT_DETAILS['dateOfBirth'], '%Y-%m-%d %H:%M:%S')
        assert passport_data['date_of_issue'] == datetime.datetime.strptime(
            VALID_PASSPORT_DETAILS['dateOfIssue'], '%Y-%m-%d %H:%M:%S')
        assert passport_data['date_of_expiry'] == datetime.datetime.strptime(
            VALID_PASSPORT_DETAILS['dateOfExpiry'], '%Y-%m-%d %H:%M:%S')
        assert passport_data['sex'].value == VALID_PASSPORT_DETAILS['sex']

    def test_passport_schema_schema_serialization_succeeds(
            self, new_passport, init_db):
        """Test passport schema serialization succeeds

         Args:
            new_passport (object): Fixture to create a new passport
        """
        passport = new_passport.save()
        passport_data = PassportSchema().dump(passport).data

        assert passport.passport_type == passport_data['passportType']
        assert passport.passport_no == passport_data['passportNumber']
        assert passport.sex.value == passport_data['sex']
        assert passport.nationality == passport_data['nationality']
        assert isinstance(passport_data['user'], dict)
