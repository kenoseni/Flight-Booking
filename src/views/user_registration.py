"""Module for users resource"""

from flask_restplus import Resource
from flask import request


from src import api
from ..models import User

from ..schemas.user import UserSchema
from ..utilities.validators.validate_request_json import validate_json_request
from ..utilities.constants import EXCLUDED_FIELDS
from ..utilities.messages.success_messages import SUCCESS_MESSAGES
from ..utilities.error_handler.request_error import request_error_message
from ..utilities.messages.error_messages import request_errors
from ..middleware import generate_token, token_required


@api.route('/users')
class UserRegistration(Resource):
    """Resource class for adding users"""

    @token_required
    @validate_json_request
    def post(self):
        """Create a user

        Raises:
            ValidationError: Used to raise exception if validation of email,

        Returns:
            (dict): Returns status, success message and relevant user details
        """

        request_data = request.get_json()

        excluded_fields = EXCLUDED_FIELDS.copy()

        user_schema = UserSchema(exclude=excluded_fields)

        # check if username or email already exists
        user = User.find_by_username_or_email(request_data)
        if user:
            request_error_message('error', request_errors[
                'already_exists'].format('username', 'email'), 400)
        # Deserialize, validate request data
        user_data = user_schema.load_object_into_schema(request_data)

        # add the new user data to the database
        user = User(**user_data).save()

        user = user_schema.dump(user).data
        access_token, refresh_token = generate_token(user)

        response = {
            "status": "success",
            "message": SUCCESS_MESSAGES['created'].format('Users'),
            "accessToken": access_token,
            "refreshToken": refresh_token,
            "data": user
        }, 201

        return response
