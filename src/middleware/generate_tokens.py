"""Module to generate token"""
from flask_jwt_extended import (
    create_access_token, create_refresh_token)


def generate_token(data):
    """Generates both access token and refresh token
    Args:
        data(object): user data
    """
    access_token = create_access_token(data)
    refresh_token = create_refresh_token(data)

    return access_token, refresh_token
