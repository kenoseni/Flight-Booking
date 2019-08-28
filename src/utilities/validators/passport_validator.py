"""Module for passport validator"""
from src.models import Passport
from ..error_handler.request_error import request_error_message
from ..messages.error_messages import request_errors


def validate_passport_details_already_exists(user_id):
    """Validates if a passport detail already exist
    Args:
        user_id(str): The user id
    Raises:
        (ValidationError): Used to raise an exception if validation
        during the creation of a passport fails
    """
    result = Passport.query.filter(Passport.user_id.ilike(
        '{0}'.format(user_id))).first()
    if result:
        request_error_message('error', request_errors[
                'exists'].format('Passport detail'), 409)
