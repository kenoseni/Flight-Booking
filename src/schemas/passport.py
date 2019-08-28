from marshmallow import fields, pre_load
from marshmallow_enum import EnumField
from marshmallow.validate import Length

from src.utilities.messages.error_messages import serialization_errors
from src.utilities.helpers import remove_whitespace_make_lowercase
from src.utilities.enums import SexEnum

from .base import BaseSchema
from .user import UserSchema


class PassportSchema(BaseSchema):
    """Passport schema"""
    user_id = fields.String(
        load_from='userId',
        error_messages={
            'required': serialization_errors['field_required']},
        load_only=True,
        required=True)
    passport_type = fields.String(
        error_messages={
            'required': serialization_errors['field_required']},
        required=True,
        load_from='passportType',
        dump_to='passportType')
    nationality = fields.String(
        required=True,
        error_messages={
            'required': serialization_errors['field_required']})
    passport_no = fields.String(
        dump_to='passportNumber',
        required=True,
        error_messages={
            'required': serialization_errors['field_required']},
        load_from='passportNumber')
    date_of_birth = fields.Date(
        required=True,
        error_messages={
            'required': serialization_errors['field_required'],
            'invalid': serialization_errors['invalid_date_time'].format(
                'dateOfBirth')},
        load_from='dateOfBirth',
        dump_to='dateOfBirth')
    date_of_issue = fields.Date(
        error_messages={
            'required': serialization_errors['field_required'],
            'invalid': serialization_errors['invalid_date_time'].format(
                'dateOfIssue')},
        required=True,
        load_from='dateOfIssue',
        dump_to='dateOfIssue')
    date_of_expiry = fields.Date(
        load_from='dateOfExpiry',
        dump_to='dateOfExpiry',
        required=True,
        error_messages={
            'required': serialization_errors['field_required'],
            'invalid': serialization_errors['invalid_date_time'].format(
                'dateOfExpiry')})
    sex = EnumField(
        SexEnum,
        load_by=EnumField.VALUE,
        dump_by=EnumField.VALUE,
        required=True,
        error='Please provide one of {values}')
    user = fields.Nested(
        UserSchema,
        only=['id', 'first_name', 'last_name', 'email', 'image_url'],
        dump_only=True)
