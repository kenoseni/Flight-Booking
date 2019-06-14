"""Module that returns a response to invalid user input"""
from src.utilities.error_handler.handle_error import ValidationError


def request_error_message(status, message, status_code):
    """Returns a response to invalid user input
    Args:
        status(str): the error status
        message(str): the error message
        status_code(int): status code of the error
    """
    raise ValidationError(
        {
            "status": status,
            "message": message
        }, status_code)
