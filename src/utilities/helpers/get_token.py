"""Module to get token from request object"""

from flask import request
from ..error_handler.request_error import request_error_message
from ..messages.error_messages import jwt_errors


def get_token(http_request=request):
    """Get token from request object

    Args:
        request (object): request object

    Returns:
        token (string): Token string

    Raises:
        ValidationError: Validation error raised when there is no token
                         or bearer keyword in authorization header
    """
    token = http_request.headers.get('Authorization')
    if not token:
        request_error_message('error', jwt_errors[
            'no_token'], 401)
    elif 'bearer' not in token.lower():
        request_error_message('error', jwt_errors[
            'no_bearer'], 401)
    token = token.split(' ')[-1]
    return token
