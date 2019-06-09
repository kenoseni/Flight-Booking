"""Mock data for user"""
import uuid

VALID_USER = {
    "id": str(uuid.uuid4()),
    'first_name': 'John',
    'last_name': 'Doe',
    'username': 'JD',
    'email': 'johndoe@gmail.com',
    'password': 'xxxxxxxxxxxxxxxx',
    'image_url': {},
}

VALID_USER_DATA = {
    'firstName': 'John',
    'lastName': 'Doe',
    'username': 'JD',
    'email': 'johndoe@gmail.com',
    'password': 'xxxxxxxxxxxxxxxx',
    'imageUrl': {},
}

INVALID_USER_DATA = {}
