"""Authorization fixtures module"""
import pytest
from src.middleware import generate_token
from src.utilities.constants import MIMETYPE, MIMETYPE_TEXT
from ..mocks.token import EXPIRED_TOKEN as expired_token


@pytest.fixture(scope='module')
def auth_header(new_user, generate_token=generate_token):
    """Fixture that creates authorization header"""
    user = new_user.save()
    data = {
        "id": user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
    }
    access_token, _ = generate_token(data)
    return {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': MIMETYPE,
        'Accept': MIMETYPE
    }


@pytest.fixture(scope='module')
def auth_header_text(new_user_two, generate_token=generate_token):
    """Fixture that creates authorization header"""
    user = new_user_two.save()
    data = {
        "id": user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
    }
    access_token, _ = generate_token(data)
    return {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': MIMETYPE_TEXT,
        'Accept': MIMETYPE_TEXT
    }


@pytest.fixture(scope='module')
def auth_header_without_bearer_in_token(
        new_user_three, generate_token=generate_token):
    """Fixture that creates authorization header"""
    user = new_user_three.save()
    data = {
        "id": user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
    }
    access_token, _ = generate_token(data)
    return {
        'Authorization': access_token,
        'Content-Type': MIMETYPE,
        'Accept': MIMETYPE
    }


@pytest.fixture(scope='module')
def auth_header_with_expired_token():
    """Fixture that creates authorization header"""
    return {
        'Authorization': 'Bearer {}'.format(expired_token),
        'Content-Type': MIMETYPE,
        'Accept': MIMETYPE
    }
