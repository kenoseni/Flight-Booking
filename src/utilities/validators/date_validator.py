from datetime import datetime, date
import dateutil.parser
from ..error_handler.request_error import request_error_message
from ..messages.error_messages import request_errors


def check_date_order(*args):
    """Verify that date values are valid and in range
        Args:
            date_of_issue (str): the validated start date
            date_of_expiry (str): the validated end date
            today (str): the current date
    """

    date_of_birth, date_of_issue, date_of_expiry = args
    today = date.today().strftime('%Y-%m-%d')

    if date_of_issue > date_of_expiry:
        request_error_message('error', request_errors[
            'invalid_date_range'].format(
                'Date of issue', 'Date of expiry'), 400)

    if date_of_birth > today:
        request_error_message('error', request_errors[
            'invalid_birthday'], 400)
