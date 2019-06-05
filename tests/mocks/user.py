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
    'is_admin': False
}
