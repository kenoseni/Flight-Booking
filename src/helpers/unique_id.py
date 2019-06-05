"""Unique id generator module"""
import uuid

def unique_uuid_generator(target):
    """A function to generate unique identifiers on insert."""
    unique_id = uuid.uuid4()
    target.id = str(unique_id)
