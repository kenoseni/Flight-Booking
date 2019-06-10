"""Module that validates if username already exist during user registration"""
from src.utilities.error_handler.handle_error import ValidationError
from src.utilities.messages.error_messages import request_errors


def username_exists(model, username):
    """Returns a response to invalid user input
    Args:
        model(instance): instance of model
        username(str): username
    """
    user = model.query.filter_by(username=username).first()
    if user:
        raise ValidationError(
            {
                "status": 'error',
                "message": request_errors['already_exists'].format(
                    'Username', username)
            }, 400)
