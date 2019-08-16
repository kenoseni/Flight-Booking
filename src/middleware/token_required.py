"""Modeule to secure all routes"""

import jwt
from flask import request
from functools import wraps
from config import app_config
from ..utilities.error_handler.request_error import request_error_message
from ..utilities.helpers.get_token import get_token
from ..utilities.messages.error_messages import jwt_errors


def token_required(func):
    """Authentication decorator. Validates token from the client

    Args:
        func (function): Function to be decorated

    Returns:
        function: Decorated function

    Raises:
        ValidationError: Validation error
    """

    @wraps(func)
    def decorated_function(*args, **kwargs):

        token = get_token()
        try:
            flask_env = app_config.FLASK_ENV
            secret_key = app_config.JWT_SECRET_KEY
            decoded_token = jwt.decode(
                token,
                secret_key,
                algorithms=['HS256'],
                options={
                    'verify_signature': True,
                    'verify_exp': True})
        except (
            ValueError,
            TypeError,
            jwt.ExpiredSignatureError,
            jwt.DecodeError,
            jwt.InvalidSignatureError,
            jwt.InvalidAlgorithmError,
            jwt.InvalidIssuerError
        ) as error:
            exception_mapper = {
                ValueError: (jwt_errors['server_error'], 500),
                TypeError: (jwt_errors['server_error'], 500),
                jwt.ExpiredSignatureError: (jwt_errors[
                                            'expired_token'], 401),
                jwt.DecodeError: (jwt_errors['invalid_token'], 401),
                jwt.InvalidIssuerError: (jwt_errors['issuer_error'], 401),
                jwt.InvalidAlgorithmError: (jwt_errors['algorithm_error'],
                                            401),
                jwt.InvalidSignatureError: (jwt_errors[
                                            'signature_error'], 500)
            }
            message, status_code = exception_mapper.get(
                type(error), (jwt_errors['server_error'], 500))
            request_error_message('error', message, status_code)
        # setting the payload to the request object and can be accessed with \
        # request.decoded_token from the view
        setattr(request, 'decoded_token', decoded_token)
        return func(*args, **kwargs)

    return decorated_function
