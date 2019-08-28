"""Module for request errors"""

REQUEST_ERROR_DICT = {
    'invalid_request': 'Invalid request object',
    'not_found': '{} not found',
    'invalid_credentials': 'Invalid username or password',
    'already_exists': '{0} or {1} already exists',
    'exists': '{0} already exists',
    'invalid_provided_date': 'Invalid date range please, {}.',
    'invalid_date_range': '{0} cannot be greater than {1}',
    'invalid_date_of_issue': 'Date of issue must be provided',
    'invalid_date_of_expiry': 'Date of expiry must be provided',
    'invalid_birthday': 'Birthday cannot be greater than today'
}
