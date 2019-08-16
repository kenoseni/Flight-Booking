"""Module for jwt errors"""

JWT_ERROR_DICT = {
    'no_token': 'Bad request. Header does not contain an authorization token.',
    'no_bearer': 'Bad request. The token should begin with the word "Bearer".',
    'server_error': 'Authorization failed. Please contact support.',
    'invalid_token': 'Authorization failed due to an Invalid token.',
    'issuer_error': 'Cannot verify the token provided as the expected issuer\
 does not match.',
    'algorithm_error': 'Cannot verify the token provided as it was signed with\
 a different algorithm.',
    'signature_error': 'Cannot verify the signature of the token provided as\
 it was signed by a non matching secret key',
    'expired_token': 'Token expired. Please login to get a new token'
}
