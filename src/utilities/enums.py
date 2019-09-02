"""Enums module"""

from enum import Enum


class SexEnum(Enum):
    """User sex enum"""
    male = 'male'
    female = 'female'


class FlightStatusEnum(Enum):
    """Flight stattus enum"""
    scheduled = 'scheduled'
    departed = 'departed'
    arrived = 'arrived'
    delayed = 'delayed'
