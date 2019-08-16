"""Module to test user registration"""
from flask import json
from src.utilities.messages.error_messages import serialization_errors
from src.utilities.messages.error_messages import request_errors
from src.models import User
from src.utilities.constants import CHARSET
from tests.mocks.user import (
    VALID_USER_DATA, INVALID_USER_DATA, NEW_USER6, NEW_USER7)
from config import app_config


BASE_URL = app_config.API_BASE_URL_V1


class TestUserRegistration:
    """Test user registration"""
    def test_user_registration_with_valid_data_succeeds(
            self, init_db, client, auth_header):
        """Should return a 201 status code, a token and user data"""
        response = client.post(
            f'{BASE_URL}/users',
            headers=auth_header,
            data=json.dumps(VALID_USER_DATA))
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 201
        assert response_json['status'] == 'success'
        assert response_json['data']['firstName'].lower() == VALID_USER_DATA[
            'firstName'].lower()
        assert response_json['data']['lastName'].lower() == VALID_USER_DATA[
            'lastName'].lower()
        assert response_json['data']['username'].lower() == VALID_USER_DATA[
            'username'].lower()
        assert response_json['data']['email'] == VALID_USER_DATA['email']
        assert response_json['data']['imageUrl'] == VALID_USER_DATA['imageUrl']

    def test_user_registration_with_invalid_data_fails(
            self, init_db, client, auth_header):
        """Should return error messages when invalid data is passed"""
        response = client.post(
            f'{BASE_URL}/users',
            headers=auth_header,
            data=json.dumps(INVALID_USER_DATA))
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 400
        assert response_json['message'] == 'An error occurred'
        assert response_json['errors']['firstName'][0] == serialization_errors[
            'field_required']
        assert response_json['errors']['lastName'][0] == serialization_errors[
            'field_required']
        assert response_json['errors']['email'][0] == serialization_errors[
            'field_required']
        assert response_json['errors']['password'][0] == serialization_errors[
            'field_required']
        assert response_json['errors']['username'][0] == serialization_errors[
            'field_required']

    def test_user_registration_with_invalid_content_type_fails(
            self, init_db, client, auth_header_text):
        """Should return an error message for invalid content type"""
        response = client.post(
            f'{BASE_URL}/users',
            headers=auth_header_text,
            data=json.dumps(VALID_USER_DATA))
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 400
        assert response_json['status'] == 'error'
        assert response_json['message'] == serialization_errors[
            'json_required']

    def test_user_registration_with_existing_username_fails(
            self, init_db, client, auth_header):
        """Should return a status code of 400 and an error message"""
        user = User(**NEW_USER6).save()
        response = client.post(
            f'{BASE_URL}/users',
            headers=auth_header,
            data=json.dumps(NEW_USER7))
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 400
        assert response_json['status'] == 'error'
        assert response_json['message'] == request_errors[
            'already_exists'].format('username', 'email')
