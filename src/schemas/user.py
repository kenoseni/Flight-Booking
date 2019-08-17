"""User schema module"""

from marshmallow import fields, pre_load
from marshmallow.validate import Length

from src.utilities.messages.error_messages import serialization_errors
from src.utilities.helpers import remove_whitespace_make_lowercase

from .base import BaseSchema


class UserSchema(BaseSchema):
    """User schema"""
    first_name = fields.String(
        required=True,
        error_messages={
            'required': serialization_errors['field_required']},
        validate=Length(min=1, max=60),
        load_from='firstName',
        dump_to='firstName')
    last_name = fields.String(
        validate=Length(min=1, max=60),
        required=True,
        error_messages={
            'required': serialization_errors['field_required']},
        load_from='lastName',
        dump_to='lastName')
    username = fields.String(
        required=True,
        error_messages={
            'required': serialization_errors['field_required']},
        validate=Length(min=1, max=60))
    email = fields.Email(
        required=True,
        error_messages={
            'required': serialization_errors['field_required']})
    password = fields.String(
        required=True,
        error_messages={
            'required': serialization_errors['field_required']},
        validate=Length(min=8, max=128),
        load_only=True)
    image_url = fields.Dict(load_from='imageUrl', dump_to='imageUrl')
    is_admin = fields.Boolean(load_only=True)

    @pre_load
    def custom_validation(self, data):
        """Removes whitespace and converts to lowercase"""
        remove_whitespace_make_lowercase(data, 'password')

    class Meta:
        """Order the output"""
        ordered = True
