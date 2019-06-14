"""Module to test user login"""
from flask import json
from src.models import User
from config import app_config
from tests.mocks.user import (
    NEW_USER, NEW_USER2, NEW_USER3, NEW_USER4, NEW_USER5,
    VALID_USER_LOGIN_DATA, VALID_USER_LOGIN_DATA2,
    INVALID_USER_LOGIN_DATA, INVALID_USER_LOGIN_DATA2,
    INVALID_USER_LOGIN_DATA3, INVALID_USER_LOGIN_DATA4)
from src.utilities.constants import CHARSET
from src.utilities.messages.error_messages import request_errors

BASE_URL = app_config.API_BASE_URL_V1

class TestUserLogin:
    """Test user login"""
    def test_user_login_with_valid_email_and_password_succeeds(
            self, init_db, client, auth_header):
        """Should return a 200 status code, tokens and user data"""
        user = User(**NEW_USER).save() 
        response = client.post(
            f'{BASE_URL}/users/login',
            headers=auth_header,
            data=json.dumps(VALID_USER_LOGIN_DATA))
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert response_json['data']['firstName'].lower() == NEW_USER['first_name'].lower()
        assert response_json['data']['lastName'].lower() == NEW_USER['last_name'].lower()
        assert response_json['data']['username'].lower() == NEW_USER['username'].lower()
        assert response_json['data']['email'] == NEW_USER['email']
        assert response_json['data']['imageUrl'] == NEW_USER['image_url']

    def test_user_login_with_valid_username_and_password_succeeds(
            self, init_db, client, auth_header):
        """Should return a 200 status code, tokens and user data"""
        user = User(**NEW_USER2).save()
        response = client.post(
            f'{BASE_URL}/users/login',
            headers=auth_header,
            data=json.dumps(VALID_USER_LOGIN_DATA2))
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert 'access_token' in response_json
        assert 'refresh_token' in response_json
        assert response_json['data']['firstName'] == user.first_name
        assert response_json['data']['lastName'] == user.last_name
        assert response_json['data']['username'] == user.username
        assert response_json['data']['email'] == user.email
        assert response_json['data']['imageUrl'] == user.image_url


    def test_user_login_with_empty_data_fails(
        self, init_db, client, auth_header):
        """Should return a 400 status code with error messages"""
        User(**NEW_USER3).save()
        response = client.post(
            f'{BASE_URL}/users/login',
            headers=auth_header,
            data=json.dumps(INVALID_USER_LOGIN_DATA))
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 400
        assert response_json['status'] == 'error'
        assert response_json['message'] == request_errors['invalid_credentials']


    def test_user_login_with_no_username_or_email_data_fails(
        self, init_db, client, auth_header):
        """Should return a 404 status code with error messages"""
        User(**NEW_USER4).save()
        response = client.post(
            f'{BASE_URL}/users/login',
            headers=auth_header,
            data=json.dumps(INVALID_USER_LOGIN_DATA2))
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 404
        assert response_json['status'] == 'error'
        assert response_json['message'] == request_errors['not_found'].format('User')


    def test_user_login_with_wrong_email_and_password_fails(
        self, init_db, client, auth_header):
        """Should return a 400 status code with error messages"""
        User(**NEW_USER5).save()
        response = client.post(
            f'{BASE_URL}/users/login',
            headers=auth_header,
            data=json.dumps(INVALID_USER_LOGIN_DATA3))
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 400
        assert response_json['status'] == 'error'
        assert response_json['message'] == request_errors['invalid_credentials']


    def test_user_login_with_empty_string_fails(
            self, client, auth_header):
        """Should return a 400 status code with error messages"""
        response = client.post(
            f'{BASE_URL}/users/login',
            headers=auth_header,
            data=json.dumps(INVALID_USER_LOGIN_DATA4))
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 400
        assert response_json['status'] == 'error'
        assert response_json['message'] == request_errors['invalid_request']
