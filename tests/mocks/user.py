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
    'firstName': 'Cristian',
    'lastName': 'Anderson',
    'username': 'CA',
    'email': 'christian@gmail.com',
    'password': 'xxxxxxxxxxxxxxxx',
    'imageUrl': {},
}

INVALID_USER_DATA = {}

NEW_USER = {
    'first_name': 'Laura',
    'last_name': 'Croft',
    'username': 'LC',
    'email': 'tombraider@gmail.com',
    'password': 'tombraider',
    'image_url': {},
}
NEW_USER2 = {
    'first_name': 'Max',
    'last_name': 'Spencer',
    'username': 'MS',
    'email': 'maxspencer@gmail.com',
    'password': 'marksandspencer',
    'image_url': {},
}

NEW_USER3 = {
    'first_name': 'Lionel',
    'last_name': 'Messi',
    'username': 'LM',
    'email': 'lionelmessi@gmail.com',
    'password': 'barcelona10',
    'image_url': {},
}

NEW_USER4 = {
    'first_name': 'Xavi',
    'last_name': 'Hanandez',
    'username': 'XH',
    'email': 'xavihanandez@gmail.com',
    'password': 'barcelona06',
    'image_url': {},
}

NEW_USER5 = {
    'first_name': 'Cristiano',
    'last_name': 'Ronaldo',
    'username': 'CR',
    'email': 'cristianoronaldo@gmail.com',
    'password': 'juventus07',
    'image_url': {},
}

NEW_USER6 = {
    'first_name': 'Sagio',
    'last_name': 'Ramos',
    'username': 'SR',
    'email': 'sagioramos@gmail.com',
    'password': 'realmadrid02',
    'image_url': {},
}

NEW_USER7 = {
    'first_name': 'Steven',
    'last_name': 'Richards',
    'username': 'SR',
    'email': 'stevenrichards@gmail.com',
    'password': 'mypassword',
    'image_url': {},
}

VALID_USER_LOGIN_DATA = {
    'email': 'tombraider@gmail.com',
    'password': 'tombraider'
}

VALID_USER_LOGIN_DATA2 = {
    'username': 'MS',
    'password': 'marksandspencer'
}
INVALID_USER_LOGIN_DATA = {}

INVALID_USER_LOGIN_DATA2 = {
    'password': 'barcelona06'
}

INVALID_USER_LOGIN_DATA3 = {
    'email': 'cristianoronaldo@gmail.com',
    'password': 'juventus007'
}

INVALID_USER_LOGIN_DATA4 = ""
