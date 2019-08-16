from flask import json
from src.models import User
from src.utilities.constants import CHARSET
from src.utilities.messages.error_messages import request_errors
from src.utilities.messages.error_messages import jwt_errors
from config import app_config
from tests.mocks.user import (
    VALID_USER_DATA)

Base_URL = app_config.API_BASE_URL_V1


class TestTokenRequired:
    """Test token required"""
    def test_token_required_without_a_token_fails(self, init_db, client):
        """Should return a 401 status code and an error message"""
        response = client.post(
            f'{Base_URL}/users',
            data=json.dumps(VALID_USER_DATA))
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 401
        assert response_json['status'] == 'error'
        assert response_json['message'] == jwt_errors['no_token']

    def test_token_required_without_bearer_in_token_fails(
            self, init_db, client, auth_header_without_bearer_in_token):
        response = client.post(
            f'{Base_URL}/users',
            headers=auth_header_without_bearer_in_token,
            data=json.dumps(VALID_USER_DATA))
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 401
        assert response_json['status'] == 'error'
        assert response_json['message'] == jwt_errors['no_bearer']

    def test_token_required_with_expired_token_fails(
            self, init_db, client, auth_header_with_expired_token):
        response = client.post(
            f'{Base_URL}/users',
            headers=auth_header_with_expired_token,
            data=json.dumps(VALID_USER_DATA))
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 401
        assert response_json['status'] == 'error'
        assert response_json['message'] == jwt_errors['expired_token']
