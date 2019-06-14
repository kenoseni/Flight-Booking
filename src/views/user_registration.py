"""Module for users resource"""

from flask_restplus import Resource
from flask import request


from src import api
from ..models import User

from ..schemas.user import UserSchema
from ..utilities.validators.validate_request_json import validate_json_request
from ..utilities.validators.username_exists import username_exists
from ..utilities.constants import EXCLUDED_FIELDS
from ..utilities.messages.success_messages import SUCCESS_MESSAGES
from ..utilities.error_handler.request_error import request_error_message
from ..utilities.messages.error_messages import request_errors
from ..middleware import generate_token


@api.route('/users')
class UserRegistration(Resource):
    """Resource class for adding users"""

    @validate_json_request
    def post(self):
        """Create a user

        Raises:
            ValidationError: Used to raise exception if validation of email,

        Returns:
            (dict): Returns status, success message and relevant user details
        """

        request_data = request.get_json()
        email = request_data.get('email', '')
        username = request_data.get('username', '').strip().lower()

        username_exists(User, username)

        excluded_fields = EXCLUDED_FIELDS.copy()

        user_schema = UserSchema(exclude=excluded_fields)

        # Deserialize, validate response data
        user_data = user_schema.load_object_into_schema(request_data)


        # check if user already exist or add the new user data to the database
        user = User.find_or_create(user_data, email=email)
        user = user_schema.dump(user).data
        access_token, refresh_token = generate_token(user)

        response = {
            "status": "success",
            "message": SUCCESS_MESSAGES['created'].format('Users'),
            "access_token": access_token,
            "refresh_token": refresh_token,
            "data": user
        }, 201

        return response
