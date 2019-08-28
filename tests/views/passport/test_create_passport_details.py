"""Module to test create passport"""

from flask import json
from src.models import Passport
from config import app_config
from src.utilities.constants import CHARSET
from src.utilities.messages.error_messages import request_errors
from tests.mocks.passport import (
    VALID_PASSPORT_DATA, VALID_PASSPORT_DATA_TWO, INVALID_PASSPORT_DATA_ONE,
    INVALID_PASSPORT_DATA_TWO, INVALID_PASSPORT_DATA_THREE)

BASE_URL = app_config.API_BASE_URL_V1


class TestCreatePassport:
    """Test create passport"""
    def test_create_passport_details_succeeds(
            self, init_db, client, auth_header, new_user):
        """Should return a 201 status code, and passport data"""
        new_user.save()
        VALID_PASSPORT_DATA['userId'] = new_user.id
        response = client.post(
            f'{BASE_URL}/passports',
            headers=auth_header,
            data=json.dumps(VALID_PASSPORT_DATA))
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 201
        assert response_json['status'] == 'success'
        assert response_json['data']['nationality'] == VALID_PASSPORT_DATA[
            'nationality']
        assert response_json['data']['passportNumber'] == VALID_PASSPORT_DATA[
            'passportNumber']

    def test_create_passport_of_existing_user_passport_fails(
            self, init_db, client, auth_header, new_user, new_passport):
        """Should return a 409 status code, and error message"""
        new_passport.save()
        VALID_PASSPORT_DATA_TWO['userId'] = new_passport.user_id
        response = client.post(
            f'{BASE_URL}/passports',
            headers=auth_header,
            data=json.dumps(VALID_PASSPORT_DATA_TWO))
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 409
        assert response_json['status'] == 'error'
        assert response_json['message'] == request_errors[
            'exists'].format('Passport detail')

    def test_create_passport_with_issue_date_greater_than_exipry_date_fails(
            self, init_db, client, auth_header, new_user_two, new_passport):
        """Should return a 400 status code, and error message"""
        new_user_two.save()
        INVALID_PASSPORT_DATA_ONE['userId'] = new_user_two.id
        response = client.post(
            f'{BASE_URL}/passports',
            headers=auth_header,
            data=json.dumps(INVALID_PASSPORT_DATA_ONE))
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 400
        assert response_json['status'] == 'error'
        assert response_json['message'] == request_errors[
            'invalid_date_range'].format('Date of issue', 'Date of expiry')

    def test_create_passport_with_date_of_birth_greater_than_today_fails(
            self, init_db, client, auth_header, new_user_three):
        """Should return a 400 status code, and error message"""
        new_user_three.save()
        INVALID_PASSPORT_DATA_TWO['userId'] = new_user_three.id
        response = client.post(
            f'{BASE_URL}/passports',
            headers=auth_header,
            data=json.dumps(INVALID_PASSPORT_DATA_TWO))
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 400
        assert response_json['status'] == 'error'
        assert response_json['message'] == request_errors[
            'invalid_birthday']

    def test_create_passport_with_invalid_user_id_fails(
            self, init_db, client, auth_header):
        """Should return a 404 status code, and error message"""
        response = client.post(
            f'{BASE_URL}/passports',
            headers=auth_header,
            data=json.dumps(INVALID_PASSPORT_DATA_THREE))
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 404
        assert response_json['status'] == 'error'
        assert response_json['message'] == request_errors[
            'not_found'].format('User')
