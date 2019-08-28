"""Module for passport resource"""

from flask_restplus import Resource
from flask import request
from src import api, db
from src.middleware import token_required
from ..models import User, Passport
from ..schemas.passport import PassportSchema
from ..utilities.validators.validate_request_json import validate_json_request
from ..utilities.constants import EXCLUDED_FIELDS
from ..utilities.messages.success_messages import SUCCESS_MESSAGES
from ..utilities.messages.error_messages import request_errors
from ..utilities.validators.passport_validator import (
    validate_passport_details_already_exists)
from ..utilities.validators.date_validator import check_date_order


@api.route('/passports')
class PassportResource(Resource):
    """Resource class for passports"""

    @token_required
    @validate_json_request
    def post(self):
        """Create passport details
        Raises:
            ValidationError: Used to raise exception

        Returns:
            (dict): Returns status, success message and relevant passport
            details
        """
        request_data = request.get_json()
        User.get_or_404_(request_data.get('userId', ''))
        validate_passport_details_already_exists(request_data['userId'])
        check_date_order(
            request_data.get('dateOfBirth', ''),
            request_data.get('dateOfIssue', ''),
            request_data.get('dateOfExpiry', ''))
        excluded_fields = EXCLUDED_FIELDS.copy()

        passport_schema = PassportSchema(exclude=excluded_fields)
        passport_data = passport_schema.load_object_into_schema(request_data)
        # add passport data to the database
        passport = Passport(**passport_data).save()

        passport = passport_schema.dump(passport).data

        response = {
            "status": "success",
            "message": SUCCESS_MESSAGES['created'].format('Passport'),
            "data": passport
        }, 201
        return response
