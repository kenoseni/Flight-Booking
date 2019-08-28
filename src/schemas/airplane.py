from marshmallow import fields, pre_load
from marshmallow.validate import Length

from src.utilities.messages.error_messages import serialization_errors
from src.utilities.helpers import remove_whitespace_make_lowercase

from .base import BaseSchema


class AirplaneSchema(BaseSchema):
    """Airplane schema"""
    model = fields.String(
        validate=Length(min=1, max=30),
        required=True,
        error_messages={
            'required': serialization_errors['field_required']})
    type = fields.String(
        validate=Length(min=1, max=40),
        error_messages={
            'required': serialization_errors['field_required']},
        required=True)
    capacity = fields.Integer(
        required=True,
        error_messages={
            'required': serialization_errors['field_required']})

    @pre_load
    def airplane_custom_validation(self, data):
        """Removes whitespace and converts to lowercase"""
        remove_whitespace_make_lowercase(data, '')
