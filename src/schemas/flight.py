from marshmallow import fields
from marshmallow_enum import EnumField
from marshmallow.validate import Length

from src.utilities.messages.error_messages import serialization_errors
from src.utilities.enums import FlightStatusEnum

from .base import BaseSchema
from .airplane import AirplaneSchema


class FlightSchema(BaseSchema):
    """Flight schema"""
    flight = fields.String(
        required=True,
        validate=Length(min=4, max=5),
        error_messages={'required': serialization_errors['field_required']})
    check_in = fields.DateTime(
        required=True,
        dump_to="checkIn",
        error_messages={
            'required': serialization_errors['field_required'],
            'invalid': serialization_errors['invalid_date_time'].format(
                'checkIn')},
        load_from='checkIn')
    departure = fields.DateTime(
        error_messages={
            'required': serialization_errors['field_required'],
            'invalid': serialization_errors['invalid_date_time'].format(
                'departure')},
        required=True)
    airplane_id = fields.String(
        load_from='airplaneId',
        load_only=True,
        required=True,
        error_messages={
            'required': serialization_errors['field_required']})
    destination = fields.String(
        error_messages={
            'required': serialization_errors['field_required']},
        required=True)
    status = EnumField(
        FlightStatusEnum,
        dump_by=EnumField.VALUE,
        load_by=EnumField.VALUE)
    airplane = fields.Nested(
        AirplaneSchema,
        dump_only=True,
        only=['id', 'model', 'type', 'capacity'])
