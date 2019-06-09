"""Module to validate for json request"""

from functools import wraps
from flask import request
from src.utilities.messages.error_messages import serialization_errors


def validate_json_request(func):
    """Decorator function to check for json content type in request"""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            return {
                'status': 'error',
                'message': serialization_errors['json_required']
            }, 400
        return func(*args, **kwargs)

    return decorated_function
