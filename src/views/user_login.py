from flask_restplus import Resource
from flask import request
from src import api
from ..models import User

from ..schemas.user import UserSchema
from ..utilities.constants import EXCLUDED_FIELDS
from ..utilities.error_handler.request_error import request_error_message
from ..utilities.validators.validate_request_json import validate_json_request
from ..utilities.messages.error_messages import request_errors
from ..utilities.messages.success_messages import SUCCESS_MESSAGES
from ..middleware import generate_token


@api.route('/users/login')
class UserLogin(Resource):
    """Resource class for user login"""

    @validate_json_request
    def post(self):
        """Create a user

        Raises:
            ValidationError: Used to raise exception if validation of email,

        Returns:
            (dict): Returns status, success message and relevant user details
        """
        request_data = request.get_json()
        try:
            password = request_data.get('password')
        except AttributeError:
            request_error_message('error', request_errors['invalid_request'], 400)
        excluded_fields = EXCLUDED_FIELDS.copy()
        user_schema = UserSchema(exclude=excluded_fields)

        if password is None:
            request_error_message('error', request_errors['invalid_credentials'], 400)

        # query user by email or password
        user = User.find_by_username_or_email(request_data)
        if user is None:
            request_error_message('error',
                                  request_errors['not_found'].format('User'), 404)

        if User.verify_password(user.password, password):
            user_details = user_schema.dump(user).data
            access_token, refresh_token = generate_token(user_details)

            response = {
                "status": "success",
                "message": SUCCESS_MESSAGES['logged_in'].format(user_details['username']),
                "access_token": access_token,
                "refresh_token": refresh_token,
                "data": user_details
            }, 200

            return response
        else:
            request_error_message('error', request_errors['invalid_credentials'], 400)
